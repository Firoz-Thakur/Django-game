from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=43)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=54)
    marks=models.IntegerField()
    pass_date=models.DateField()