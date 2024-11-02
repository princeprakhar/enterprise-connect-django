from django.db import models

# Create your models here.
class Company(models.Model):
  company_id = models.AutoField(primary_key= True)
  name= models.CharField(max_length=30)
  company = models.CharField(max_length=30)
  location = models.CharField(max_length=30) 
  about = models.TextField()
  type = models.CharField(max_length=30,choices=[('public','Public'),('private','Private')])
  date = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)
  
class Employee():
  employee_id = models.AutoField(primary_key= True)
  name= models.CharField(max_length=30)
  username = models.EmailField()
  password = models.CharField(max_length=30,unique=True)
  company = models.CharField(max_length=30)
  about = models.TextField()
  