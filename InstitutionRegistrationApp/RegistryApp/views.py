import re
from django import forms
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user, allowed_users
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.generic import TemplateView

from .forms import patientregistration_form
from .forms import studentregistration_form
from .forms import hospitalstaffregistration_form
from .forms import schoolstaffregistration_form
from .forms import hospitalregistration_form
from .forms import schoolsregistration_form

from .models import patientregistrationformdb
from .models import studentregistrationformdb
from .models import hospitalstaffregistrationformdb
from .models import schoolstaffregistrationformdb
from .models import hospitalregistrationformdb
from .models import schoolsregistrationformdb

# Create your views here.
# EXAMPLE

# def (request):
#     return render(request, 'RegistryApp/Schools/.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# PAGES


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def SelectionPage(request):
    return render(request, 'RegistryApp/Pages/SelectionPage.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def RegistrationFormsPage(request):
    return render(request, 'RegistryApp/Pages/RegistrationFormsPage.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def RegistrationReportsPage(request):
    return render(request, 'RegistryApp/Pages/RegistrationReportsPage.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def MapPage(request):
    return render(request, 'RegistryApp/Pages/MapPage.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def base(request):
    return render(request, 'RegistryApp/base.html')

# FORMS
# Hospitals


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def HospitalRegistrationForm(request):
    if request.method == "POST":
       form = hospitalregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('HospitalRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Hospitals/HospitalRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = hospitalregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Hospitals/HospitalRegistrationForm.html',context)

# Schools


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def SchoolsRegistrationForm(request):
    if request.method == "POST":
       form = schoolsregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('SchoolsRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Schools/SchoolsRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = schoolsregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Schools/SchoolsRegistrationForm.html',context)

# Personel
# Hospital
# Patient


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def PatientRegistrationForm(request):
    if request.method == "POST":
       form = patientregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('PatientRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Personel/Hospital/Patient/PatientRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = patientregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Personel/Hospital/Patient/PatientRegistrationForm.html',context)

# Staff


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def HospitalStaffRegistrationForm(request):
    if request.method == "POST":
       form = hospitalstaffregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('HospitalStaffRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Personel/Hospital/Staff/HospitalStaffRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = hospitalstaffregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Personel/Hospital/Staff/HospitalStaffRegistrationForm.html',context)

# School
# Staff


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def SchoolStaffRegistrationForm(request):
    if request.method == "POST":
       form = schoolstaffregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('SchoolStaffRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Personel/School/Staff/SchoolStaffRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = schoolstaffregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Personel/School/Staff/SchoolStaffRegistrationForm.html',context)

# Students


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar'])
def StudentsRegistrationForm(request):
    if request.method == "POST":
       form = studentregistration_form(request.POST)

       if form.is_valid():
          post = form.save(commit=False)
          post.save()
          return redirect('StudentsRegistrationForm')
       else:
       # this should be include if form validate failed
          return render(request, 'RegistryApp/Forms/Personel/School/Students/StudentsRegistrationForm.html', {'form': form})

    elif request.method == "GET":
        form = studentregistration_form()
        context = {'form': form}
        # return render(request, 'index.html', context)
    return render(request, 'RegistryApp/Forms/Personel/School/Students/StudentsRegistrationForm.html',context)

# REPORTS
# Hospitals


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def HospitalReport(request):
    context = {'HospitalReport': hospitalregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/Hospital/HospitalReport.html', context)

# School


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def SchoolReport(request):
    context = {'SchoolReport': schoolsregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/School/SchoolReport.html', context)

# Personel
# Hospital


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def HospitalStaffReport(request):
    context = {'HospitalStaffReport': hospitalstaffregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/Personel/Hospital/HospitalStaffReport.html', context)


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def PatientReport(request):
    context = {'PatientReport': patientregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/Personel/Hospital/PatientReport.html', context)

# School


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def SchoolStaffReport(request):
    context = {'SchoolStaffReport': schoolstaffregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/Personel/School/SchoolStaffReport.html', context)


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','registrar','viewer'])
def StudentReport(request):
    context = {'StudentReport': studentregistrationformdb.objects.all()}
    return render(request, 'RegistryApp/Reports/Personel/School/StudentReport.html', context)

# HOME
# Other


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def home_example(request):
    return render(request, 'RegistryApp/home.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def about(request):
    return render(request, 'RegistryApp/Forms/Home/about.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def contact(request):
    return render(request, 'RegistryApp/Forms/Home/contact.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    return render(request, 'RegistryApp/Forms/Home/index.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def loginform(request):
    return render(request, 'RegistryApp/Forms/Home/loginform.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def services(request):
    return render(request, 'RegistryApp/Forms/Home/services.html')
