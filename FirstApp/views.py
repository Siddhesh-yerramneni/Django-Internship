from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from FirstApp.models import Register
# Create your views here.
def home(request):
    return HttpResponse("Hello World")
def ht(request):
    return HttpResponse("<h2>Hello World</h2>")
def usernameprint(request,uname):
    return HttpResponse("<h3>Hello World <span style='color:green'>{}</span></h3>".format(uname))
def us(request,uname,age):
    return HttpResponse("<h3>Hi {} and your age is {}</h3>".format(uname,age))
def empdetails(request,eid,ename,eage):
    return HttpResponse("<h3><script>alert('hi welcome {}')</script>hi Welcome {} your age is {} and your empid is {}</h3>".format(ename,ename,eage,eid))
def htm(request):
    return render(request,'html/sample.html')
def html(request, uname):
    return render(request,'html/sample1.html',{'n':uname})
def details(request,uname,id):
    y={'n':uname,'i':id}
    return render(request,'html/sample2.html',y)

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')
def myform(request):
    if request.method == "POST":
        #print(request.POST)

        uname = request.POST['uname'] # prints individual data
        rollno = request.POST['rollno'] # prints individual data
        email = request.POST['email'] # prints individual data and also can use POST.get('VarName')
        #print(uname,rollno,email)

        data = {'username':uname,'rno':rollno,'email':email}
        return render(request,'html/display.html',data)
    return render(request,'html/myform.html')

def reg(req):
    if req.method=="POST":
        fn = req.POST['fn']
        ln=req.POST['ln']
        email=req.POST['email']
        phone=req.POST['phone']
        gender=req.POST['gender']
        address=req.POST['address']
        language=req.POST['language']
        hob=req.POST['hob']
        regdata = {'firstname':fn,'lastname':ln,'email':email,'number':phone,'gender':gender,'address':address,'language':language,'hobbies':hob}
        return render(req,'html/output.html',regdata)
    return render(req,'html/register.html')

def register(req):
    if req.method=="POST":
        fn = req.POST['fn']
        ln=req.POST['ln']
        email=req.POST['email']
        phone=req.POST['phone']
        gender=req.POST['gender']
        address=req.POST['address']
        language=req.POST['language']
        regdata = {'firstname':fn,'lastname':ln,'email':email,'number':phone,'gender':gender,'address':address,'language':language,}
        return render(req,'html/output.html',regdata)
    return render(req,'html/Register.html')

def log(req):
    if req.method=="POST":
        uname=req.POST['uname']
        pwd=req.POST['pwd']
        if(uname=="User" and pwd=="poiuytrewq"):
            return HttpResponse("<h3><script>alert('Valid')</script></h3>")
        else:
            return HttpResponse("<h3><script>alert('Invalid')</script></h3>")
    
    return render(req,'html/login.html')

def register2(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        reg= Register(name = name, email = email)
        reg.save()
    return render(req,'html/register2.html')

def display(req):
    data=Register.objects.all()
    return render(req,'html/display1.html',{'data':data})

def sview(request,y):
    w = Register.objects.get(id=y)
    return render(request,'html/sview.html',{'y':w})

def supt(request,q):
    t=Register.objects.get(id=q)
    if request.method=="POST":
        na=request.POST['n']
        em=request.POST['e']
        t.name=na
        t.email=em
        t.save()
        return redirect('/display')
    return render(request,'html/supdate.html',{'p':t})

def sdel(request,z):
    b=Register.objects.get(id=z)
    if request.method=="POST":
        b.delete()
        return redirect('/display')
    return render(request,'html/sndlt.html',{'a':b})
