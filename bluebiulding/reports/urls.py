from django.contrib import admin
from django.urls import path
from bluebiulding.reports import views

app_name="reports"

urlpatterns = [
    path('', views.index, name='index'),
    path('exhibition/', views.exhibition, name='exhibition')
]