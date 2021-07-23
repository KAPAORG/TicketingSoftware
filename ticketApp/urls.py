from django.contrib import admin
from django.urls import path
from ticketApp import views

urlpatterns = [
    path('', views.dashboard),
    path('my_open_issues/', views.my_open_issues),
    path('reported_by_me/', views.reported_by_me),
    path('create_ticket/', views.create_ticket),
    path('my_projects/', views.my_projects),
]
