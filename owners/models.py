import datetime
from xmlrpc.client import DateTime
from django.db import models

from app.models import Customer


# Create your models here.
class Owners(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    court_name = models.CharField(max_length=30)
    sports_type = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=15)
    booking_no = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=10 ,default='requested')
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'owners'


class Turf(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(Owners, on_delete=models.CASCADE)
    profile_image = models.ImageField( upload_to='profile/')
    bg_image = models.ImageField(upload_to='background/')
    first_image = models.ImageField( upload_to='turf/')
    second_image = models.ImageField(upload_to='turf/')
    third_image = models.ImageField( upload_to='turf/')

    class Meta:
        db_table = 'turf'


class Slote(models.Model):
    id = models.AutoField(primary_key=True)
    turf_id = models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    # slote = models.TimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'slote'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    turf_id = models.ForeignKey(Turf, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20,default='NULL')
    payment = models.FloatField(default=0000)
    status = models.CharField(max_length=10,default='availabe')

    class Meta:
        db_table = 'booking'
        







