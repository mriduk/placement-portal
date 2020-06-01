from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from company_cell.models import company
from registers.models import Student
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.models import User,auth
import xlwt
# from .forms import placementform

# def showCompanies(request):
#     allCompanies=company.objects.all()
#     print(allCompanies)
#     # return HttpResponse(request,"Heyyyy")
#     return render(request, 'accounts/companies.html', {'allCompanies': allCompanies})
class showCompanies(ListView):
    template_name = 'accounts/companies.html'
    context_object_name = 'companies_list'
    

    def get_queryset(self):
        """Return the last five published questions."""
        return company.objects.all()

class comp_detail(DetailView):
    
    model=company
    
    template_name='accounts/company_detail.html'

def count_stud(request,comp_id,username):
    stud=User.objects.get(username=username)
    stud1=Student.objects.get(user=stud)
    print(stud1.name)
    print(stud1.company)
    comp=get_object_or_404(company,pk=comp_id)
    print(comp.comp_id)
    print(comp. no_of_students_applied)
    comp. no_of_students_applied=comp. no_of_students_applied+1
    comp.save()
    stud1.company=comp
    stud1.save()
    
    
    return render(request,'first_page/base.html')

def recruit(request):
    return render(request,'recruit.html')


    

def profile(request,username):
    # username = get_object_or_404(User, username=username)
    stud=User.objects.get(username=username)
    stud1=Student.objects.get(user=stud)
   
    print(username)
    print(stud1.name)
    print(stud1.regno)
    args={'stud1':stud1}
    return render(request,'welcome.html',args)






    








# def applyjob(request):
    
#     if request.method == 'post':
#         form=placementform(request.POST,request.FILES)
#         if form.is_valid():
#             instance=form.save(commit=False)
#             instance.student=Student
#             print(request.user.username)
#             instance.save()
#             return render(request,'accounts/company1.html')
#     else:
#         form=placementform()
#     return render(request,'accounts/company1.html',{'form':form})

# def applyjob(request):
#     stud=get_object_or_404(Student,pk=regno)

def back_home(request):
    return render(request,'first_page/base.html')

    



    
# Create your views here.
