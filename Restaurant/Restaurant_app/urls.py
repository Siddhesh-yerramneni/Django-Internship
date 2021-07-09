from django.urls import path
from django.urls.resolvers import URLPattern
from Restaurant_app import views
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnct/',views.contact,name="ct"),
    path('rlist/',views.reslist, name="rstl"),
    path('rst/<int:m>/',views.rstup,name="rsup"),
    path('rdlt/<int:m>/',views.rstdel,name="rdel"),
    path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
    path('ilist/',views.itlist,name="itl"),
    path('iupdate/<int:n>/',views.itemupdate,name="iup"),
    path('idel/<int:m>/',views.itdel,name="idel"),
    path('rg/',views.usrreg,name="reg"),
    path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
    path('logout',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
    path('roletype/',views.rolereq,name="rlrq"),
    path('gvper/',views.gveperm,name="gvpm"),
    path('gvup/<int:t>/',views.gvupd,name="gvup"),
    path('pfle/',views.pfle,name="pf"),
    path('fbd',views.feedback,name="fd"),
]