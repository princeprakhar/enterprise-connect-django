from django.db import models

# Create your models here.
class company():
  company_id = models.AutoField(primary_key= True)
  name= models.CharField(max_length=30)
  username = models.EmailField()
  password = models.CharField(max_length=30,unique=True)
  company = models.CharField(max_length=30)
  about = models.TextField()
  

  