from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_pets, name='search_pets'),
    
    # Report pets
    path('report/found/', views.report_found_pet, name='report_found_pet'),
    path('report/lost/', views.report_lost_pet, name='report_lost_pet'),
    path('report/success/<int:pet_id>/', views.report_success, name='report_success'),
    
    # Pet details
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    
    # Admin
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/request/<int:request_id>/update/', views.update_request_status, name='update_request_status'),
]