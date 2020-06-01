from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from .views import show_notification
urlpatterns = [
   
    url('show_notification',show_notification.as_view(),name='show_notification'),
    
    
]