from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pet, Contact

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
class FoundPetForm(forms.ModelForm):
    date_found = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    class Meta:
        model = Pet
        fields = ['type', 'breed', 'color', 'location', 'description', 'image']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Golden Retriever'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Golden Brown'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Central Park, NY'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the pet...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image file size must be under 5MB")
            if not image.content_type.startswith('image'):
                raise forms.ValidationError("Only image files are allowed")
        return image

class LostPetForm(forms.ModelForm):
    date_lost = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    class Meta:
        model = Pet
        fields = ['pet_name', 'type', 'breed', 'color', 'location', 'owner_contact', 'description', 'image']
        widgets = {
            'pet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pet\'s name'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Labrador'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Black'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last seen location'}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone or Email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your pet...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        labels = {
            'pet_name': 'Pet Name',
            'owner_contact': 'Your Contact Information',
            'location': 'Last Seen Location',
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this about?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Your message...'}),
        }