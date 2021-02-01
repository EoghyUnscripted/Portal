from django.urls import path, include

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='tip-dashboard'),
    path('calculate/', views.tips, name='tip-calculate'),
]