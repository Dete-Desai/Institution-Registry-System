from django.shortcuts import render

# Create your views here.

#Authentication
def Login(request):
    return render(request, 'accounts/Authentication/LoginForm.html')

#Home
def Home(request):
    return render(request, 'accounts/Home/Home.html')
