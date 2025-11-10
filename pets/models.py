from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom User Model
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Pet Model
class Pet(models.Model):
    PET_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('rabbit', 'Rabbit'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('adopted', 'Adopted'),
        ('reunited', 'Reunited'),
    ]

    type = models.CharField(max_length=20, choices=PET_TYPES)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='pets/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reported_date = models.DateTimeField(auto_now_add=True)
    date_found = models.DateField(blank=True, null=True)  # New field
    date_lost = models.DateField(blank=True, null=True)   # New field
    pet_name = models.CharField(max_length=100, blank=True)  # For lost pets
    owner_contact = models.CharField(max_length=100, blank=True)  # For lost pets
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reported_date']

    def __str__(self):
        return f"{self.type} - {self.breed} ({self.status})"


# Request Model
class Request(models.Model):
    REQUEST_TYPES = [
        ('adoption', 'Adoption Request'),
        ('inquiry', 'Inquiry'),
        ('report', 'Report'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_type} by {self.user.username} for {self.pet}"