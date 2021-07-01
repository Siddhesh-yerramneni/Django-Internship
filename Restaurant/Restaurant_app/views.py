from Restaurant_app.models import Restaurents
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Restaurant_app.forms import ReForm
from django.contrib import messages
# Create your views here.
def home(request):
    w = Restaurents.objects.all()
    return render(request,'app/homee.html',{'c':w})

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def login(request):
    return render(request,'app/login.html')

def reslist(request):
    y = Restaurents.objects.all()
    if request.method == "POST":
        t = ReForm(request.POST,request.FILES)
        if t.is_valid():
            t.save()
            messages.success(request,"Restaurant added Successfully")
            return redirect('/rlist')
    t = ReForm()
    return render(request,'app/restlist.html',{'q':t, 'a':y})

def rstup(request,m):
    k=Restaurents.objects.get(id=m)
    if request.method=="POST":
        e=ReForm(request.POST,request.FILES,instance=k)
        if e.is_valid():
            e.save()
            messages.success(request,"{} Restaurant updates succesfully!".format(k.Rname))
            return redirect('/rlist')
    e=ReForm(instance=k)
    return render(request,'app/restupdate.html',{'x':e})

def rstdel(request,m):
    r=Restaurents.objects.get(id=m)
    if request.method=="POST":
        messages.info(request,"Restaurant deleted")
        r.delete()
        return redirect('/rlist')
    e=ReForm(instance=r)
    return render(request,'app/rstdel.html',{'a':e})

def rstvw(request,a):
    s = Restaurents.objects.get(id=a)
    return render(request,'app/restview.html',{'z':s})
