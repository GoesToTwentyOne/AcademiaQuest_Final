from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='Student/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    user.is_staff = True
  
    
    def __str__(self):
        return self.user.first_name