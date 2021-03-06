from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('homeexample/', views.home_example, name='homeexample'),
]