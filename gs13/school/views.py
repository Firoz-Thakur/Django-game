from django.shortcuts import render
from .models import student
from django.views.generic.detail import DetailView
# Create your views here.
#detail veiwc
class  studentdetialview(DetailView):
    model=student
