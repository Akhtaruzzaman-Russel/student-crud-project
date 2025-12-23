from django.db import models

# Create your models here.
class StudentInfoModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    course=models.CharField(max_length=100,null=True)
    address=models.TextField(null=True)