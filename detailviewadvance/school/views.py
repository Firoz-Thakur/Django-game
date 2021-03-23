from django.shortcuts import render
from .models import student
from django.views.generic.detail import DetailView
# Create your views here.
#detail veiwc
class  studentdetialview(DetailView):
    model=student
    template_name='school/student1.html'
    context_object_name='stu' # by default is table name
  #  pk_url_kwarg='newid'
  
