from django.db import models

# Create your models here.
class Restaurents(models.Model):
    Rname=models.CharField(max_length=30)
    nitems=models.IntegerField()
    time=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rsimg = models.ImageField(upload_to='Restaurantimages/',default='logo.png')
