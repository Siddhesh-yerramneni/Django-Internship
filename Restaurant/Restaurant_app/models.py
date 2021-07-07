from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurents(models.Model):
    Rname=models.CharField(max_length=30)
    nitems=models.IntegerField()
    time=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rsimg = models.ImageField(upload_to='Restaurantimages/',default='logo.png')
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Rname

class Itemlist(models.Model):
    y=[('Non-veg','Non-veg'),('Veg', 'Veg'),('Select item-type', 'Select item-type')] 
    p=[('Available','Available'),('Not-Available', 'Not-Available'),('Select Availability', 'Select Availability')]
    iname=models.CharField(max_length=50)
    icategory=models.CharField(choices=y,default="Select item-type",max_length=50)
    price=models.DecimalField(decimal_places=3,max_digits=10)
    iimage=models.ImageField(upload_to='Itemimages/',default='logo.png')
    iavail=models.CharField(choices=p,default="Select Availability",max_length=50)
    rsid = models.ForeignKey(Restaurents,on_delete=models.CASCADE)