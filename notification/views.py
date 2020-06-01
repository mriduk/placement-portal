from django.shortcuts import render,redirect


from django.views.generic.list import ListView
from .models import notification

from django.contrib.auth.models import User,auth




class show_notification(ListView):
    
    # template_name = 'notification/notification.html'
    template_name = 'notification/notification.html'
    context_object_name = 'notifs'
    

    def get_queryset(self):
        """Return the last five published questions."""
        return notification.objects.all()