
from django.contrib import admin
from django.urls import path
from too import views

urlpatterns = [
    path('', views.show)
]
