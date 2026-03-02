from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registreren/', views.registreer, name='register'),
    path('zoeken/', views.zoek, name='zoek'),
    path('zoekhistorie/', views.zoekhistorie, name='zoekhistorie'),
]
