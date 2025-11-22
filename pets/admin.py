from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, Request, Notification, Contact

admin.site.register(User, UserAdmin)
admin.site.register(Pet)
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(Contact)