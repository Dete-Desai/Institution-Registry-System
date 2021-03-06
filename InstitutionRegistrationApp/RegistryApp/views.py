from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#EXAMPLE
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#HOME
def home_example(request):
    return render(request, 'RegistryApp/home.html')

