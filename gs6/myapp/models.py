from django.db import models

# Create your models here
from django.contrib.auth.models import User

#class User(models.Model)

class Page(models.Model):
    #user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=54)
    page_publish_date=models.DateField()

