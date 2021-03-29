from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ProdList, ProdEntry

# URL Requests
@login_required(login_url='portal/login')
def dashboard(request):
    
    context = {}
    return render(request, 'todo/dashboard.html', context)

@login_required(login_url='portal/login')
def add(request):
    
    context = {}
    return render(request, 'todo/dashboard.html', context)

@login_required(login_url='portal/login')
def edit(request):
    
    context = {}
    return render(request, 'todo/dashboard.html', context)

@login_required(login_url='portal/login')
def delete(request):
    
    context = {}
    return render(request, 'todo/dashboard.html', context)

@login_required(login_url='portal/login')
def view(request):
    
    context = {}
    return render(request, 'todo/dashboard.html', context)