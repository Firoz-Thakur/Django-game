from django.shortcuts import render
from .models import student
from django.views.generic.detail import DetailView
# Create your views here.
#detail veiw and list view
from django.views.generic.list import ListView

class  studentdetialview(DetailView):
    model=student

class studentListview(ListView):
      model=student
  
