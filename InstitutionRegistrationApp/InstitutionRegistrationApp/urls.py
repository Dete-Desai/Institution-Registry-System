"""InstitutionRegistrationApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from accounts.views import Login,Registration,LogOut, Home
# from RegistryApp.views import Charts

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminpage/', admin.site.urls),
    path('', include('RegistryApp.urls')),

    #Authentication
    path('Login/', Login, name='Login'),
    path('Registration/', Registration, name='Registration'),
    path('Logout/', LogOut, name='Logout'),
    
    # Home
    path('', Home, name='Home'),
]
