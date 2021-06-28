from django.urls import path
from django.urls.resolvers import URLPattern
from Restaurant_app import views
urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnct/',views.contact,name="ct"),
    path('log/',views.login,name="log"),
]