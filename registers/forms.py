from django import forms
from registers.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signinform(UserCreationForm):
 
    class Meta:
        model = User
        fields = ('username','password1','password2')
    


class registerform(forms.ModelForm):
    # branches=[('CSE','CSE'),('Mechanical','Mechanical'),('Electrical','EEE')]
    # choice=[('Btech','Btech'),('BBA','BBA'),('B.J.M.C','B.J.M.C'),('MTECH','MTECH')]
    name = forms.CharField()
    regno = forms.IntegerField()
    email=forms.EmailField()
    course=forms.CharField()
    branch=forms.CharField()
    phno=forms.IntegerField()
    parent_name=forms.CharField()
    parent_phno=forms.IntegerField()
    cgpa=forms.IntegerField()
    backlogs=forms.IntegerField()

    
   
    class Meta:
        
        model = Student
        fields = ('name','regno','email','course','branch','phno','parent_name','parent_phno','cgpa','backlogs',)






