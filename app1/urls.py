"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.home, name='home'),
    # path('',views.home.as_view(),name='home'),
    path('add', views.add, name='add'),
    path('details/<slug:p>/', views.details, name='details'),
    path('delete/<slug:l>/', views.delete, name='delete'),
    path('edit/<slug:e>/', views.edit, name='edit')
]
