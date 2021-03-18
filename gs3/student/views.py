from django.shortcuts import render

def setsession(request):
    request.session['name']='baaba ji'
    request.session['game']='15 lakh ki game bnani'
    request.session['acha']='hein macho'
    return render(request,'student/setsession.html')


def getsession(request):
    name=request.session['name']
    keys=request.session.keys()

    return render(request,'student/getsession.html',{'name':name,'keys':keys})
  
def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')
