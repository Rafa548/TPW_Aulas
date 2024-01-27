"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from BookStore import views

urlpatterns = [
    path('booksearch/',views.booksearch, name='booksearch'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('lista/', views.lista_liv, name='lista_liv'),
    path('liv_details/<str:name>', views.liv_details, name='liv_details',),
    path('lista_aut/', views.lista_aut, name='lista_aut'),
    path('aut_details/<str:name>', views.aut_details, name='aut_details', ),
    path('lista_liv_author/<str:name>', views.lista_liv_author, name='lista_liv_author', ),
]
