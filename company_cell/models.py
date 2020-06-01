from django.db import models



class company(models.Model):
    profiles=[('Technical','Technical'),('Non Technical','Non Technical'),('Both','Both')]
    comp_id=models.IntegerField(primary_key=True)
    image=models.ImageField(upload_to='post-image/',blank=True)
    comp_name=models.CharField(max_length=50)
    job_profile=models.CharField(max_length=254,choices=profiles)
    status=[('In process','In process'),('Closed','Closed'),('Coming soon','Coming soon')]
    comp_status=models.CharField(choices=status,max_length=254)
    no_of_students_applied=models.IntegerField(default=0)

    def image_url(self):
            if self.image:
                    return self.image.url
            return "/static/images/one.jpeg"

            



    def __str__(self):
            return self.comp_name

    
    class Meta:
        verbose_name = "Comapany"
        verbose_name_plural = "Companies"

# class company_stud(models.Model):
#         company=models.ForeignKey(company,on_delete=models.CASCADE)
#         no_of_students=models.IntegerField(default=0)



# class student_and_comp(models.Model):
#     company=models.ForeignKey(company,on_delete=models.CASCADE)
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
    

#     def __str__(self):
#         return self.student.name


        

