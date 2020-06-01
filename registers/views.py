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

from pkgutil import get_data

import xlwt


def test(request):

    subject = 'Welcome to DataFlair'
    message = 'Hope you are enjoying your Django Tutorials'
    recepient = "mriduk.00@gmail.com"
    send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        
    return render(request, '/')



def signin(request):
    
    
    if request.method == 'POST':
        form = signinform(request.POST)
        profile_form = registerform(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            print(profile.email)
            subject = 'Welcome to Manipal University Jaipur Placement Portal'
            message = 'Welcome to Manipal University Jaipur Placement Portal. You have succesfully created your account!'
           
            recepient = str(profile.email)
            send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            print("done")
          
            # return render(request,"accounts/profile.html")
            return render(request,'created.html')
          
    else:
        form = signinform()
        profile_form = registerform()
    args={'form':form,'profile_form':profile_form}
    print("not")
    return render(request, 'signin.html',args)



def profile(request,username):
    # username = get_object_or_404(User, username=username)
    stud=User.objects.get(username=username)
    stud1=Student.objects.get(user=stud)
   
    print(username)
    print(stud1.name)
    print(stud1.regno)
    args={'stud1':stud1}
    return render(request,'welcome.html',args)



    
   

# def update(request):
#     if request.method == 'POST':
#         form = registerform(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             name=form.cleaned_data.get('name')
#             # return render(request,"accounts/updated_profile.html")
#             print(name)
#             return render(request,"accounts/updated_profile.html")
#     else:
#         form = registerform(instance=request.user)
#     args={'form':form}
#     return render(request, 'update.html', args)

# class profile(DetailView):
#     model=Student
#     template_name = 'accounts/profile.html'
#     print(Student.name)

    


# def profile(request):
#     args={'user':request.user}
#     return render(request,'accounts/profile.html',args)

    # def update(request):
#     if request.method == 'POST':
#         form = registerform(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             name=form.cleaned_data.get('name')
#             # return render(request,"accounts/updated_profile.html")
#             print(name)
#             return HttpResponse("Hey")
#     else:
#         form = registerform(instance=request.user)
#         args={'form':form}
#         return render(request, 'update.html', args)



def download_excel_data(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['NAME', 'EMAIL', 'BRANCH', 'REGNO', ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = Student.objects.all()
    
  #dummy method to fetch data.
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.name, font_style)
		ws.write(row_num, 1, my_row.email, font_style)
		ws.write(row_num, 2, my_row.branch, font_style)
		ws.write(row_num, 3, my_row.regno, font_style)
        

	wb.save(response)
	return response


   

        



# Create your views here.
