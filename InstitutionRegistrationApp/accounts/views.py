from django.shortcuts import render

# Create your views here.

#Authentication
def Login(request):
    return render(request, 'accounts/login.html')

#Home
def Home(request):
    return render(request, 'accounts/index.html')
