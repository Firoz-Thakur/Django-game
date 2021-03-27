from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
   #students_data=student.objects.all()
   # students_data=student.objects.filter(marks=54),having onnly 54 marks
   #students_data=student.objects.exclude(marks=54),not having 54 marks
  # students_data=student.objects.order_by('roll')
   #students_data=student.objects.order_by('-roll')
  # students_data=student.objects.order_by('?') randomly
  # students_data=student.objects.order_by('id').reverse()[0:5]
   #students_data=student.objects.values('name','city')
 #  students_data=student.objects.values('name','city')  gives us dictionary
   return render(request,'school/home.html',{'stus':students_data})