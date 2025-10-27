from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, Request

admin.site.register(User, UserAdmin)
admin.site.register(Pet)
admin.site.register(Request)