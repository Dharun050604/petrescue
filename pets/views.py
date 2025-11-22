from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import UserRegistrationForm, UserLoginForm, FoundPetForm, LostPetForm, ContactForm
from .models import Pet, Request, User, Notification, Contact

def create_notification(user, notification_type, title, message, related_request=None):
    """Helper function to create notifications"""
    Notification.objects.create(
        user=user,
        notification_type=notification_type,
        title=title,
        message=message,
        related_request=related_request
    )

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'pets/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'pets/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'pets/profile.html')


def home(request):
    recent_pets = Pet.objects.all().order_by('-reported_date')[:6]
    return render(request, 'pets/home.html', {'recent_pets': recent_pets})


@login_required
def report_found_pet(request):
    if request.method == 'POST':
        form = FoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.reported_by = request.user
            pet.status = 'found'
            pet.date_found = form.cleaned_data.get('date_found')
            pet.save()
            
            # Create a request entry
            pet_request = Request.objects.create(
                user=request.user,
                pet=pet,
                request_type='report',
                status='pending',
                message=f'Found pet reported: {pet.breed}'
            )
            
            # Notify all admin users
            admin_users = User.objects.filter(is_staff=True)
            for admin in admin_users:
                create_notification(
                    user=admin,
                    notification_type='new_request',
                    title='New Found Pet Report',
                    message=f'{request.user.username} reported a found {pet.breed}',
                    related_request=pet_request
                )
            
            messages.success(request, 'Pet reported successfully! Waiting for admin approval.')
            return redirect('report_success', pet_id=pet.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FoundPetForm()
    
    return render(request, 'pets/report_found.html', {'form': form})


@login_required
def report_lost_pet(request):
    if request.method == 'POST':
        form = LostPetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.reported_by = request.user
            pet.status = 'lost'
            pet.date_lost = form.cleaned_data.get('date_lost')
            pet.save()
            
            # Create a request entry
            pet_request = Request.objects.create(
                user=request.user,
                pet=pet,
                request_type='report',
                status='pending',
                message=f'Lost pet reported: {pet.pet_name or pet.breed}'
            )
            
            # Notify all admin users
            admin_users = User.objects.filter(is_staff=True)
            for admin in admin_users:
                create_notification(
                    user=admin,
                    notification_type='new_request',
                    title='New Lost Pet Report',
                    message=f'{request.user.username} is looking for their lost {pet.pet_name or pet.breed}',
                    related_request=pet_request
                )
            
            messages.success(request, 'Lost pet reported! We\'ll help you find your companion.')
            return redirect('report_success', pet_id=pet.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LostPetForm()
    
    return render(request, 'pets/report_lost.html', {'form': form})


@login_required
def report_success(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, reported_by=request.user)
    return render(request, 'pets/report_success.html', {'pet': pet})


def search_pets(request):
    query = request.GET.get('q', '')
    pet_type = request.GET.get('type', '')
    breed = request.GET.get('breed', '')
    color = request.GET.get('color', '')
    location = request.GET.get('location', '')
    status = request.GET.get('status', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    # Start with all pets
    pets = Pet.objects.all()
    
    # Apply filters
    if query:
        pets = pets.filter(
            Q(breed__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(pet_name__icontains=query)
        )
    
    if pet_type:
        pets = pets.filter(type=pet_type)
    
    if breed:
        pets = pets.filter(breed__icontains=breed)
    
    if color:
        pets = pets.filter(color__icontains=color)
    
    if location:
        pets = pets.filter(location__icontains=location)
    
    if status:
        pets = pets.filter(status=status)
    
    if date_from:
        pets = pets.filter(
            Q(date_found__gte=date_from) | Q(date_lost__gte=date_from)
        )
    
    if date_to:
        pets = pets.filter(
            Q(date_found__lte=date_to) | Q(date_lost__lte=date_to)
        )
    
    # Order by most recent
    pets = pets.order_by('-reported_date')
    
    # Pagination
    paginator = Paginator(pets, 12)
    page_number = request.GET.get('page')
    pets_page = paginator.get_page(page_number)
    
    context = {
        'pets': pets_page,
        'query': query,
        'selected_type': pet_type,
        'selected_status': status,
        'total_results': pets.count(),
    }
    
    return render(request, 'pets/search.html', context)


@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Get similar pets (same type and within similar time frame)
    similar_pets = Pet.objects.filter(
        type=pet.type,
        status=pet.status
    ).exclude(id=pet.id)[:4]
    
    # Check if user can contact (logged in and not the reporter)
    can_contact = request.user.is_authenticated and request.user != pet.reported_by
    
    context = {
        'pet': pet,
        'similar_pets': similar_pets,
        'can_contact': can_contact,
    }
    
    return render(request, 'pets/pet_detail.html', context)


@staff_member_required
def admin_dashboard(request):
    status_filter = request.GET.get('status', 'pending')
    
    requests_list = Request.objects.select_related('user', 'pet').filter(
        status=status_filter
    ).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(requests_list, 10)
    page_number = request.GET.get('page')
    requests_page = paginator.get_page(page_number)
    
    # Count statistics
    stats = {
        'pending': Request.objects.filter(status='pending').count(),
        'approved': Request.objects.filter(status='approved').count(),
        'rejected': Request.objects.filter(status='rejected').count(),
    }
    
    context = {
        'requests': requests_page,
        'current_status': status_filter,
        'stats': stats,
    }
    
    return render(request, 'pets/admin_dashboard.html', context)


@staff_member_required
def update_request_status(request, request_id):
    if request.method == 'POST':
        pet_request = get_object_or_404(Request, id=request_id)
        new_status = request.POST.get('status')
        
        if new_status in ['approved', 'rejected']:
            pet_request.status = new_status
            pet_request.save()
            
            # Notify the user who made the request
            status_emoji = '✅' if new_status == 'approved' else '❌'
            create_notification(
                user=pet_request.user,
                notification_type='status_update',
                title=f'Request {new_status.title()}',
                message=f'{status_emoji} Your report for {pet_request.pet.breed} has been {new_status}',
                related_request=pet_request
            )
            
            messages.success(request, f'Request {new_status} successfully!')
        else:
            messages.error(request, 'Invalid status')
    
    return redirect('admin_dashboard')

@login_required
def user_dashboard(request):
    # Get all pets reported by the current user
    my_pets = Pet.objects.filter(reported_by=request.user).order_by('-reported_date')
    
    # Get all requests made by the user
    my_requests = Request.objects.filter(user=request.user).select_related('pet').order_by('-created_at')
    
    # Statistics
    stats = {
        'total_reports': my_pets.count(),
        'found_pets': my_pets.filter(status='found').count(),
        'lost_pets': my_pets.filter(status='lost').count(),
        'pending': my_requests.filter(status='pending').count(),
        'approved': my_requests.filter(status='approved').count(),
        'rejected': my_requests.filter(status='rejected').count(),
    }
    
    context = {
        'my_pets': my_pets,
        'my_requests': my_requests,
        'stats': stats,
    }
    
    return render(request, 'pets/user_dashboard.html', context)


@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, reported_by=request.user)
    
    # Check if pet request is still pending
    pet_request = Request.objects.filter(pet=pet, user=request.user, status='pending').first()
    if not pet_request:
        messages.error(request, 'You can only edit pending requests.')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        if pet.status == 'found':
            form = FoundPetForm(request.POST, request.FILES, instance=pet)
        else:
            form = LostPetForm(request.POST, request.FILES, instance=pet)
        
        if form.is_valid():
            pet = form.save(commit=False)
            if pet.status == 'found':
                pet.date_found = form.cleaned_data.get('date_found')
            else:
                pet.date_lost = form.cleaned_data.get('date_lost')
            pet.save()
            
            messages.success(request, 'Pet information updated successfully!')
            return redirect('user_dashboard')
    else:
        if pet.status == 'found':
            form = FoundPetForm(instance=pet)
        else:
            form = LostPetForm(instance=pet)
    
    context = {
        'form': form,
        'pet': pet,
    }
    
    return render(request, 'pets/edit_pet.html', context)


@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, reported_by=request.user)
    
    # Check if pet request is still pending
    pet_request = Request.objects.filter(pet=pet, user=request.user, status='pending').first()
    if not pet_request:
        messages.error(request, 'You can only delete pending requests.')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        pet_name = pet.pet_name or pet.breed
        pet.delete()
        messages.success(request, f'🗑️ Report for {pet_name} has been deleted.')
        return redirect('user_dashboard')
    
    return render(request, 'pets/delete_pet.html', {'pet': pet})

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user)
    unread_count = user_notifications.filter(is_read=False).count()
    
    # Pagination
    paginator = Paginator(user_notifications, 20)
    page_number = request.GET.get('page')
    notifications_page = paginator.get_page(page_number)
    
    context = {
        'notifications': notifications_page,
        'unread_count': unread_count,
    }
    
    return render(request, 'pets/notifications.html', context)


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    
    # Redirect to related page if exists
    if notification.related_request:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    
    return redirect('notifications')


@login_required
def mark_all_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    messages.success(request, 'All notifications marked as read')
    return redirect('notifications')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            
            # Notify admins
            admin_users = User.objects.filter(is_staff=True)
            for admin in admin_users:
                create_notification(
                    user=admin,
                    notification_type='message',
                    title='New Contact Message',
                    message=f'New message from {contact_message.name}: {contact_message.subject}'
                )
            
            messages.success(request, '📧 Message sent successfully! We\'ll get back to you soon.')
            return redirect('contact_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Pre-fill form if user is logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = ContactForm(initial=initial_data)
    
    return render(request, 'pets/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'pets/contact_success.html')