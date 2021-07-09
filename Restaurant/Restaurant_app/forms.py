from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from Restaurant_app.models import Restaurents, Itemlist, Rolereq, User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReForm(ModelForm):
    class Meta:
        model= Restaurents
        fields = ["Rname","nitems","time","rsimg","address"]
        widgets = {
            "Rname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter the name",
            }),
            "nitems":forms.TextInput(attrs={
                "class":"form-control my-2",
			"placeholder":"Enter Number of Items available in Restaurant",
            }),
            "time":forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":3,
			}),
        }

class ItemsForm(forms.ModelForm):
    class Meta:
        model=Itemlist
        fields = ["rsid","iname","icategory","price","iavail","iimage"]
        widgets = {
            "rsid":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Select Restaurant",
                #"readonly":True
            }),
            "iname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter name",
            }),
            "icategory":forms.Select(attrs={
               "class":"form-control my-2",
            }),
            "price":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price",
            }),
            "iavail":forms.Select(attrs={
                "class":"form-control my-2",
            })
        }

class usgform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"Enter Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"ConfirmPassword",
    }))
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
        }


class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["Uname","rltype","pfe"]
        widgets= {
            # "uname":forms.TextInput(attrs={
            #     "class":"form-control my-2",
            #     "readonly":True,
            # }),
            "rltype":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True,
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }