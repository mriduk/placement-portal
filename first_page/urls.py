from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    url('contact_msg/',views.contact_msg,name='contact_msg'),
    url('recruit/',views.recruit, name='recruit'),
    
    
    
]