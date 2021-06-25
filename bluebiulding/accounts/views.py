from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from .models import PasswordReset
from django.contrib import messages
from bluebiulding.reports.models import Report
from bluebiulding.reports.api import cryptoAPI

User = get_user_model()

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    object_list = Report.objects.filter(name=request.user)
    context = {
        'object_list': object_list,
    }
    return render(request, template_name, context)

@login_required
def dashboardDetails(request, pk):
    template_name = 'reports/exhibition.html'
    name=request.user
    id = int(pk)
    user_report = Report.objects.filter(name=request.user, id=pk)

    your_name = str(user_report[0].name)
    cryptocurrency = str(user_report[0].cryptocurrency.symbol)

    print(your_name)

    context = cryptoAPI(your_name, cryptocurrency)

    return render(request, template_name, context)

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username = user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form      
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados da sua conta foram alterados com sucesso')
            return redirect('accounts:dashboard')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
