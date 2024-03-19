from django.urls import path
from .views import admin_login, home

urlpatterns = [
    path('/', admin_login, name='admin_login'),
    path('home/', home, name='home'),  # Add this line if 'home' is your home page view
    # Add other URL patterns as needed
]
