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


  def __str__(self):
    return self.name + ' - ' + self.company
  
class Employee(models.Model):
  name= models.CharField(max_length=30)
  username = models.EmailField()
  password = models.CharField(max_length=30,unique=True)
  location = models.CharField(max_length=250)
  position = models.CharField(max_length=30,choices=(('manager','Manager'),('developer','Developer'),('student','Student')))
  company = models.ForeignKey(Company,on_delete=models.CASCADE)
  about = models.TextField()
  