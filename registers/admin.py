from django.contrib import admin
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from django.http import HttpResponse
from registers.forms import signinform,registerform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registers.models import Student
from placement.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404

from .models import Student

def confirmed(modeladmin, request, queryset):
        queryset.update(status='PLACED')
        confirmed.short_description = "Mark selected Students as comfirmed!"


def not_confirmed(modeladmin, request, queryset):
        queryset.update(status='NOT PLACED')
        not_confirmed.short_description = "Mark selected Students as not comfirmed!"

def mail(modeladmin,request,queryset):

        subject = 'You have registered'
        message = 'GET THE HELL IN!'
        for i in queryset:
                recepient = str(i.email)
                send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                print("done")


class Student1(admin.ModelAdmin):
    list_display = ['name', 'regno','email','status']
    list_filter=['status','branch','company',]
    ordering = ['name','regno','status']
    actions = [confirmed,not_confirmed,mail]
    save_as = True
    save_on_top = True
    change_list_template = 'admin/change_list_graph.html'

    

    

admin.site.register(Student,Student1)



