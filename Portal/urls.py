from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.signup, name='portal'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('portal/', views.portal, name='portal'),
    path('todo/', include('ToDo.urls')),
]