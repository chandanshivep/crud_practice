from django.db import models 
from django.contrib.auth.models import User
class Record(models.Model):
    owner =models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    city =models.CharField(max_length=100)
    phone =models.CharField(max_length=15)
    def __str__(self):
       return self.name

