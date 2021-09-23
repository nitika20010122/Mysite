from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home, name='home'),
    path('about us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('plant my tree', views.plant, name='plant'),
    path('team', views.team, name='team'),
    path('ourprojects', views.ourprojects, name='ourprojects'),
    path('home', views.home, name='home'),
    path('send', views.send, name='send'),
    path('read more', views.about, name='about'),
  ]
