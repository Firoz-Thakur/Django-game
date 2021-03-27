from  django import forms

class Contactform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    msg=forms.CharField(widget=forms.Textarea)