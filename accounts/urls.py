from django.urls import path
from django.contrib.auth import views as auth_views # Import Django's auth views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    
    # Add the login URL
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # Add the logout URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Add the dashboard URL
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
