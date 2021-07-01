from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from Restaurant_app.models import Restaurents

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