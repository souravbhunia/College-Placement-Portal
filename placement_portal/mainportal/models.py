from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    email=models.EmailField()
    
    
    
    HS_marks=models.IntegerField()
    current_cgpa=models.IntegerField()
    current_backlogs=models.CharField()
   