from django.shortcuts import render
from django.views.generic.list import ListView
from .models import student
# Create your views here.
class StudentListView(ListView):
    model=student #_list is bydefalut
    ordering=['name']
  #  template_name_suffix='_get' for this we also need the tempalte with name student_get
    template_name='school/student.html'
    context_object_name='student'  #we can use the custom object name 