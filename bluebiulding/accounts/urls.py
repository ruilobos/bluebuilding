from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from bluebiulding.accounts import views

app_name="accounts"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<pk>', views.dashboardDetails, name='dashboard_detail'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('edit-password/', views.edit_password, name='edit_password'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-confirm/(^?P<key>\w+)$/', views.password_reset_confirm, name='password_reset_confirm'),
]