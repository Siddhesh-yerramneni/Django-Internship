from django.db.models.base import Model
from django.forms import ModelForm
from Restaurant_app.models import Restaurents

class ReForm(ModelForm):
    class Meta:
        model= Restaurents
        fields = "__all__"