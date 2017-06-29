from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    college= models.CharField(max_length=200)

    def __str__(self):
        return self.username

   
class contactus(models.Model):
    email = models.EmailField(max_length=200)
    #password = models.CharField(max_length=200)
    name= models.CharField(max_length=300)
    message= models.CharField(max_length=9000)

    def __str__(self):
        return self.email

class students(models.Model):
    name=models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    course=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    experience=models.TextField(max_length=11000)
    
    def __str__(self):
        return self.name
