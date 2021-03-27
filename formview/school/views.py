from django.shortcuts import render
from .forms import Contactform
# Creafrte your views here.
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
class contactformview(FormView):
    template_name='school/contactform.html'
    form_class=Contactform
    success_url='/thanku/'

class thankyou(TemplateView):
    template_name='school/thankyou.html'
    

