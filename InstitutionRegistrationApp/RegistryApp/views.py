from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# EXAMPLE

# def (request):
#     return render(request, 'RegistryApp/Schools/.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# PAGES


def SelectionPage(request):
    return render(request, 'RegistryApp/Pages/SelectionPage.html')

# FORMS
# Hospitals


def HospitalRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Hospitals/HospitalRegistrationForm.html')

# Schools


def SchoolsRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Schools/SchoolsRegistrationForm.html')

# Personel
# Hospital
# Patient


def PatientRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Personel/Hospital/Patient/PatientRegistrationForm.html')

# Staff


def HospitalStaffRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Personel/Hospital/Staff/HospitalStaffRegistrationForm.html')

# School
# Staff


def SchoolStaffRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Personal/School/Staff/SchoolStaffRegistrationForm.html')

# Students


def StudentsRegistrationForm(request):
    return render(request, 'RegistryApp/Forms/Personal/School/Students/StudentsRegistrationForm.html')

# REPORTS
# Hospitals


def HospitalReport(request):
    return render(request, 'RegistryApp/Reports/Hospital/HospitalReport.html')

# School


def SchoolReport(request):
    return render(request, 'RegistryApp/Reports/School/SchoolReport.html')

# Personel
# Hospital


def HospitalStaffReport(request):
    return render(request, 'RegistryApp/Reports/Personel/Hospital/HospitalStaffReport.html')


def PatientReport(request):
    return render(request, 'RegistryApp/Reports/Personel/Hospital/PatientReport.html')

# School


def SchoolStaffReport(request):
    return render(request, 'RegistryApp/Reports/Personel/School/SchoolStaffReport.html')


def StudentReport(request):
    return render(request, 'RegistryApp/Reports/Personel/School/StudentReport.html')

# HOME
# Other


def home_example(request):
    return render(request, 'RegistryApp/home.html')


def about(request):
    return render(request, 'RegistryApp/Forms/Home/about.html')


def base(request):
    return render(request, 'RegistryApp/Forms/Home/base.html')


def contact(request):
    return render(request, 'RegistryApp/Forms/Home/contact.html')


def index(request):
    return render(request, 'RegistryApp/Forms/Home/index.html')


def loginform(request):
    return render(request, 'RegistryApp/Forms/Home/loginform.html')


def services(request):
    return render(request, 'RegistryApp/Forms/Home/services.html')
