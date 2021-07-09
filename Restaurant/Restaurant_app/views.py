from Restaurant_app.models import Restaurents, Itemlist, Rolereq, User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Restaurant_app.forms import ItemsForm, ReForm, Rlupd, usgform, Rltype
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Restaurant import settings
# Create your views here.
def home(request):
    w = Restaurents.objects.filter(uid_id=request.user.id)
    return render(request,'app/homee.html',{'c':w})

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def login(request):
    return render(request,'app/login.html')

@login_required
def reslist(request):
    y = Restaurents.objects.filter(uid_id=request.user.id)
    if request.method == "POST":
        t = ReForm(request.POST,request.FILES)
        if t.is_valid():
            c = t.save(commit=False)
            c.uid_id = request.user.id
            c.save()
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

@login_required
def itlist(request):
    st =list(Restaurents.objects.filter(uid_id=request.user.id))
    mm=Itemlist.objects.all()
    d,i={},0
    for mp in mm:
        for h in st:
            if h.id == mp.rsid_id:
                d[i] = mp.iname, mp.icategory,mp.price,mp.iimage,mp.iavail,mp.id,h.Rname
                i = i+1
    if request.method == "POST":
        k=ItemsForm(request.POST,request.FILES)
        if k.is_valid():
            n=k.save(commit=False)
            n.save()
            messages.success(request,'Item added')
            return redirect('/ilist/')
    k=ItemsForm()        
    return render(request,'app/itmlist.html',{'r':k,'er':st, 's':d.values()})

def itemupdate(request,n):
    a=Itemlist.objects.get(id=n)
    if request.method=="POST":
        s=ItemsForm(request.POST,request.FILES,instance=a)
        if s.is_valid():
            s.save()
            return redirect('/ilist')
    s=ItemsForm(instance=a)
    return render(request,'app/update.html',{'y':s})

def itdel(request,m):
    r=Itemlist.objects.get(id=m)
    if request.method=="POST":
        r.delete()
        messages.success(request,"{} Restaurent Deleted Successfully".format(r.iname))
        return redirect('/ilist')
    e=ItemsForm(instance=r)
    return render(request,'app/itdel.html',{'a':e})

def usrreg(request):
    if request.method == "POST":
        d = usgform(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d=usgform()
    return render(request,'app/userregister.html',{'t':d})

@login_required
def rolereq(request):
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k = Rltype(request.POST,request.FILES)
        if k.is_valid():
            y = k.save(commit=False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            print(y)
            y.save()
            # return redirect('/')
    k = Rltype()
    return render(request,'app/rolereq.html',{'d':k, 'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d={}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id :
                continue
            else:
                d[m.id] = m.Uname, m.rltype, n.role,n.id
    return render(request,'app/gvpl.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y = Rolereq.objects.get(ud_id=t)
    d = User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'app/gvepermission.html',{'c':n})

@login_required
def pfle(request):
    return render(request,'app/profile.html')

@login_required
def feedback(request):
    if request.method == "POST":
        sd = request.POST['snmail'].split(',')
        sm = request.POST['sub']
        mg = request.POST['msg']
        rt = settings.EMAIL_HOST_USER
        dt = send_mail(sm,mg,rt,sd)
        if dt == 1:
            return redirect('/')
    return render(request,'app/feedback.html')
