from django.shortcuts import render
from django.views import View
from .forms import contactform
from django.http import HttpResponse
# Create your views here.
def homefun(request):
    return render(request,'school/home.html')


class HomeClassView(View):
    def get(self, request):
        return render(request,'school/home.html')

def aboutfun(request):
    context={'msg':'welcome to geeky shows eyh'}
    return render(request,'school/about.html',context)

class AboutClassView(View):
    def get(self, request):
         context={'msg':'welcome to geeky shows eyh'}
         return render(request,'school/about.html',context)

def contatfun(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thankyou form submited")
    else:
        form=contactform()
    return render(request,'school/contact.html',{'form':form})

class contactclassview(View):
    def get(self, request):
        form=contactform()
        return render(request,'school/contact.html',{'form':form})
    
    def post(self,request):
        form=contactform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thankyou form submited")
        return render(request,'school/contact.html',{'form':form})


def newsfun(request):
    context={'info':'cbi enquiry why geekyshows earn less money'}
    return render(request,'school/news.html',context)