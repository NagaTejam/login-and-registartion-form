from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('signup/', views.signup,  name='signup'),
    path('logout/', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    path('profile/', views.view_profile,  name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    
]