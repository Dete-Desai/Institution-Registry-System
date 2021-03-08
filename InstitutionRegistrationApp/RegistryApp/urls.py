from django.urls import path

from . import views

urlpatterns = [
    # path('', views., name=''),
    path('homeexample/', views.home_example, name='homeexample'),
    path('SelectionPage/', views.SelectionPage, name='SelectionPage'),
    path('HospitalRegistrationForm/', views.HospitalRegistrationForm, name='HospitalRegistrationForm'),
    path('SchoolsRegistrationForm/', views.SchoolsRegistrationForm, name='SchoolsRegistrationForm'),
    path('PatientRegistrationForm/', views.PatientRegistrationForm, name='PatientRegistrationForm'),
    path('HospitalStaffRegistrationForm/', views.HospitalStaffRegistrationForm, name='HospitalStaffRegistrationForm'),
    path('SchoolStaffRegistrationForm/', views.SchoolStaffRegistrationForm, name='SchoolStaffRegistrationForm'),
    path('StudentsRegistrationForm/', views.StudentsRegistrationForm, name='StudentsRegistrationForm'),
    path('HospitalReport/', views.HospitalReport, name='HospitalReport'),
    path('SchoolReport/', views.SchoolReport, name='SchoolReport'),
    path('HospitalStaffReport/', views.HospitalStaffReport, name='HospitalStaffReport'),
    path('PatientReport/', views.PatientReport, name='PatientReport'),
    path('SchoolStaffReport/', views.SchoolStaffReport, name='SchoolStaffReport'),
    path('StudentReport/', views.StudentReport, name='StudentReport'),

    # OTHER
    path('home_example/', views.home_example, name='home_example'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('loginform/', views.loginform, name='loginform'),
    path('services/', views.services, name='services'),
]