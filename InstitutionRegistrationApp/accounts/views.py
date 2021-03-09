import re
from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View

# Create your views here.

# AUTHENTICATION

# Create your views here.

# Authentication


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('SelectionPage')
        else:
            messages.info(request, 'Username Entered Could be Wrong: ' +username)
            messages.info(request, 'Password Entered Could be Wrong: ' +password)

    context = {}
    return render(request, 'accounts/Authentication/LoginForm.html',context)

#Registration
# @login_required(login_url='Login')
#@allowed_users(allowed_roles=['admin'])
# @admin_only
def Registration(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='viewer')
            user.groups.add(group)

            messages.success(request, 'Account Created Successfully for ' + username)
            return redirect('Login')
    context = {'form': form,}
    return render(request, 'accounts/Authentication/RegistrationForm.html',context)

#LogOut
def LogOut(request):
    logout(request)
    return redirect('Login')

# Home
def Home(request):
    return render(request, 'accounts/Home/Home.html')
