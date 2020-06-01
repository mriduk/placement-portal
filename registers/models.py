from django.db import models
from django.contrib.auth.models import User
from company_cell.models import company






class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    branches=[('CSE','CSE'),('Mechanical','Mechanical'),('ECE','ECE'),('EEE','EEE'),('Mechatronics','Mechatronics'),('Chemical','Chemical'),('IT','IT'),]
    choice=[('Btech','Btech'),('BBA','BBA'),('B.J.M.C','B.J.M.C'),('MTECH','MTECH')]
    status_lists=[('PLACED','PLACED'),('NOT PLACED','NOT PLACED')]
    name = models.CharField(max_length=200,null=False)
    regno = models.IntegerField(primary_key=True)
    email=models.EmailField(null=False,max_length=254,default=None)
    course=models.CharField(choices=choice,max_length=254,null=True)
    branch=models.CharField(max_length=254,choices=branches)
    phno=models.IntegerField(null=True)
    parent_name=models.CharField(max_length=254,null=True)
    parent_phno=models.IntegerField(null=True)
    cgpa=models.IntegerField(null=False,default=0)
    backlogs=models.IntegerField(default=0,null=True)
    company= models.ForeignKey(company, on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50,choices=status_lists)


    def __str__(self):
            return self.name
 

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

        





        
    
    


  

     
 
