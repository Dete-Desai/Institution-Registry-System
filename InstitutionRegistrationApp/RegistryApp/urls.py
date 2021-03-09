from django.urls import path

from . import views

urlpatterns = [
    # path('', views., name=''),
    # MAIN
    path('base/', views.base, name='base'),
    path('homeexample/', views.home_example, name='homeexample'),

    # PAGE
    path('SelectionPage/', views.SelectionPage, name='SelectionPage'),
    path('RegistrationFormsPage/', views.RegistrationFormsPage, name='RegistrationFormsPage'),
    path('RegistrationReportsPage/', views.RegistrationReportsPage, name='RegistrationReportsPage'),
    path('MapPage/', views.MapPage, name='MapPage'),

    path('HospitalRegistrationForm/', views.HospitalRegistrationForm, name='HospitalRegistrationForm'),
    path('SchoolsRegistrationForm/', views.SchoolsRegistrationForm, name='SchoolsRegistrationForm'),
    path('PatientRegistrationForm/', views.PatientRegistrationForm, name='PatientRegistrationForm'),
    path('HospitalStaffRegistrationForm/', views.HospitalStaffRegistrationForm, name='HospitalStaffRegistrationForm'),
    path('SchoolStaffRegistrationForm/', views.SchoolStaffRegistrationForm, name='SchoolStaffRegistrationForm'),
    path('StudentsRegistrationForm/', views.StudentsRegistrationForm, name='StudentsRegistrationForm'),
    path('HospitalReport/', views.HospitalReport, name='HospitalReport'),
    path('SchoolsReport/', views.SchoolReport, name='SchoolsReport'),
    path('HospitalStaffReport/', views.HospitalStaffReport, name='HospitalStaffReport'),
    path('PatientReport/', views.PatientReport, name='PatientReport'),
    path('SchoolStaffReport/', views.SchoolStaffReport, name='SchoolStaffReport'),
    path('StudentReport/', views.StudentReport, name='StudentReport'),

    # OTHER
    path('home_example/', views.home_example, name='home_example'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('loginform/', views.loginform, name='loginform'),
    path('services/', views.services, name='services'),
]