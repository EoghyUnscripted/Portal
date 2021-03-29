from django.urls import path, include

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='prod-dashboard'),
    path('dashboard/add/', views.add, name='prod-add'),
    path('dashboard/view/', views.view, name='prod-view'),
    path('dashboard/delete/<int:prod_id>', views.delete, name='prod-delete'),
]