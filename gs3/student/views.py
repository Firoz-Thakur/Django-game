from django.shortcuts import render

def setsession(request):
    request.session['name']='baaba ji'
    request.session['game']='15 lakh ki game bnani'
    request.session['acha']='hein macho'
    return render(request,'student/setsession.html')



def getsession(request):
    name=request.session['name']
    keys=request.session.keys()
    items=request.session.items()
    return render(request,'student/getsession.html',{'name':name,'keys':keys,'items':items,'age':'age'})
  
def delsession(request):
    request.session.flush()
    return render(request,'student/delsession.html')
