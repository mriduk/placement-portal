from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from registers.models import Student

def home(request):
    return render(request,"first_page/base.html")

def recruit(request):
    return render(request,'recruit.html')






def contact_msg(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['despandeydoga@gmail.com'], 
		 fail_silently=True)
		print("sucess")
	return render(request, 'contact_msg.html')




# Create your views here.
