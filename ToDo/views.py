from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from datetime import datetime, time, timedelta

from .models import ToDoList

# URL Requests
@login_required(login_url='/login')
def dashboard(request):
    todo = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=0)
    completed = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=1)
    tcount = todo.count()
    ccount = completed.count()
    context = {'todo':todo, 'completed':completed, 'tcount':tcount, 'ccount':ccount}
    return render(request, 'todo/dashboard.html', context)

@login_required(login_url='/login')
def add(request):
    if request.method == 'POST':
        if (request.POST['title'] and request.POST['date']):
            ToDo = ToDoList()
            ToDo.ToDo_Author = request.user
            ToDo.ToDo_Title = request.POST['title']
            ToDo.ToDo_Time = request.POST['date']
            ToDo.ToDo_Location = request.POST['location']
            ToDo.ToDo_Description = request.POST['description']
            ToDo.ToDo_Completed = 0
            ToDo.save()
            return redirect('todo-dashboard')
        else:
            return render(request, 'todo/add.html', {'error':'Title and Date are required!'})
    else:
        tcount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=0).count()
        ccount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=1).count()
        context = {'tcount':tcount, 'ccount':ccount}
        return render(request, 'todo/add.html', context)

@login_required(login_url='/login')
def edit(request, todo_id):
    if request.method == 'POST':
        if (request.POST['title'] and request.POST['date']):
            ToDo = ToDoList.objects.get(pk=todo_id)
            ToDo.ToDo_Author = request.user
            ToDo.ToDo_Title = request.POST['title']
            ToDo.ToDo_Time = request.POST['date']
            ToDo.ToDo_Location = request.POST['location']
            ToDo.ToDo_Description = request.POST['description']
            ToDo.ToDo_Completed = 0
            ToDo.save()
            return redirect('todo-dashboard')
        else:
            tcount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=0).count()
            ccount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=1).count()
            todo = get_object_or_404(ToDoList, pk=todo_id)
            context = {'todo':todo, 'tcount':tcount, 'ccount':ccount, 'error':'Could not update.'}
            return render(request, 'todo/edit.html', context)
    else:
        tcount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=0).count()
        ccount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=1).count()
        todo = get_object_or_404(ToDoList, pk=todo_id)
        context = {'todo':todo, 'tcount':tcount, 'ccount':ccount}
        return render(request, 'todo/edit.html', context)

@login_required(login_url='/login')
def view(request):
    todo = ToDoList.objects.filter(ToDo_Author=request.user)
    tcount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=0).count()
    ccount = ToDoList.objects.filter(ToDo_Author=request.user).filter(ToDo_Completed=1).count()
    context = {'tcount':tcount, 'ccount':ccount, 'todo':todo}
    return render(request, 'todo/view.html', context)

@login_required(login_url='/login')
def delete(request, todo_id):
        ToDo = get_object_or_404(ToDoList, pk=todo_id)
        ToDo.delete()
        return redirect('todo-dashboard')

@login_required(login_url='/login')
def complete(request, todo_id):
        delta = timedelta(hours=8)
        ToDo = get_object_or_404(ToDoList, pk=todo_id)
        ToDo.ToDo_Completed = 1
        ToDo.ToDo_Complete_Date = timezone.now() - delta
        ToDo.save()
        return redirect('todo-dashboard')