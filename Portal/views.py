from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Demo

# Sign Up Form
def signup(request):
    if request.method == 'POST':
        # User Submits New Form
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Check If User Exists
                user  = User.objects.get(username=request.POST['username'])
                return render(request, 'portal/login.html', {'username_error':'That username has already been taken!'})
            except User.DoesNotExist:
                # Create New User If User Does Not Exist
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], 
                                                first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                auth.login(request, user)
                username = request.POST['username']
                welcome = 'Welcome to your portal, %s!' % (request.POST['first_name'])
                demos = Demo.objects
                context = {'username':username, 'messages':welcome, 'demos':demos }
                return render(request, 'portal/portal.html', context)
        else:
            # Password Error
            return render(request, 'portal/login.html', {'password_error':'Your passwords do not match.'})
    else:
        # Checks If User Is Already Logged In
        if request.user.is_authenticated:
            return redirect('portal')
        else:
            # If User Not Logged In
            return render(request, 'portal/login.html')

# Log In Form
def login(request):
    if request.method == 'POST':
        # User Sends Username & Password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # Checks If Username & Password Match System
            auth.login(request, user)
            username = request.POST['username']
            return redirect('portal')
        else:
            # Log In Error
            return render(request, 'portal/login.html', {'login_error':'The username or password is incorrect.'})
    else:
        # Checks If User Is Already Logged In
        if request.user.is_authenticated:
            return redirect('portal')
        else:
            # If User Not Logged In
            return render(request, 'portal/login.html')

# User Sign Out
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

# User Portal
@login_required(login_url='/login')
def portal(request):
    # Loads Demo Applications On User Portal
    demos = Demo.objects
    context = {'demos':demos}
    return render(request, 'portal/portal.html', context)