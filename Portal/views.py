from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Demo

# URL Requests
def signup(request):
    if request.method == 'POST':
        # The user submitted for a new account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user  = User.objects.get(username=request.POST['username'])
                return render(request, 'portal/login.html', {'username_error':'That username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], 
                                                first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                auth.login(request, user)
                username = request.POST['username']
                welcome = 'Welcome to your portal, %s!' % (request.POST['first_name'])
                demos = Demo.objects
                context = {'username':username, 'messages':welcome, 'demos':demos }
                return render(request, 'portal/portal.html', context)
        else:
            return render(request, 'portal/login.html', {'password_error':'Your passwords do not match.'})
    else:
        if request.user.is_authenticated:
            return redirect('portal')
        else:
            return render(request, 'portal/login.html')

@login_required(login_url='/login')
def portal(request):
    demos = Demo.objects
    context = {'demos':demos}
    return render(request, 'portal/portal.html', context)

def login(request):
    if request.method == 'POST':
        # The user submitted username and password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            username = request.POST['username']
            return redirect('portal')
        else:
            return render(request, 'portal/login.html', {'login_error':'The username or password is incorrect.'})
    else:
        if request.user.is_authenticated:
            return redirect('portal')
        else:
            return render(request, 'portal/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')