from django.urls import path, include

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='todo-dashboard'),
    path('dashboard/add/', views.add, name='todo-add'),
    path('dashboard/view/', views.view, name='todo-view'),
    path('dashboard/edit/<int:todo_id>', views.edit, name='todo-edit'),
    path('dashboard/completed/<int:todo_id>', views.complete, name='todo-complete'),
    path('dashboard/delete/<int:todo_id>', views.delete, name='todo-delete'),
]