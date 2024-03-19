from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_login(request):
    if request.user.is_superuser:
        # Redirect to the admin login page for superusers
        return redirect('admin:login')
    else:
        # Redirect to the home page for non-superusers
        return redirect('home')


def home(request):
    return render(request,'home.html')