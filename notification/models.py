from django.db import models

class notification(models.Model):
    title=models.CharField(max_length=500,default='')
    description=models.TextField()
    date_time=models.DateTimeField()


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    