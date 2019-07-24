from django.contrib import admin
from django.urls import path, include
from .views import registration
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import UserView

urlpatterns = [
    path('register/', registration, name="registration_url"),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('profile/', login_required(UserView.as_view()), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
]