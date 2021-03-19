from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def myview(request):
    return HttpResponse('<h1> Funciton based view')

#class based view

class myView(View):
    name='firoz'
    def get(self,reqeust):
        return HttpResponse('<h1> class based based view')
    

class MyViewChild(myView):
    def get(self, request):
        return HttpResponse(self.name)
