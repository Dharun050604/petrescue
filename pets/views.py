from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import UserRegistrationForm, UserLoginForm, FoundPetForm, LostPetForm
from .models import Pet, Request, User


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
            Request.objects.create(
                user=request.user,
                pet=pet,
                request_type='report',
                status='pending',
                message=f'Found pet reported: {pet.breed}'
            )
            
            messages.success(request, '🎉 Pet reported successfully! Waiting for admin approval.')
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
            Request.objects.create(
                user=request.user,
                pet=pet,
                request_type='report',
                status='pending',
                message=f'Lost pet reported: {pet.pet_name or pet.breed}'
            )
            
            messages.success(request, '🙏 Lost pet reported! We\'ll help you find your companion.')
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
    return render(request, 'pets/pet_detail.html', {'pet': pet})


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
            
            messages.success(request, f'Request {new_status} successfully!')
        else:
            messages.error(request, 'Invalid status')
    
    return redirect('admin_dashboard')