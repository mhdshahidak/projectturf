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
    profile_image = models.ImageField(upload_to='profile/')
    bg_image = models.ImageField(upload_to='background/')
    first_image = models.ImageField(upload_to='turf/first')
    second_image = models.ImageField(upload_to='turf/second')
    third_image = models.ImageField(upload_to='turf/third')

    class Meta:
        db_table = 'owners'

class Slote(models.Model):
    id = models.AutoField(primary_key=True)
    turf_id = models.ForeignKey(Owners, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    slote = models.TimeField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'slote'

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    turf_id = models.ForeignKey(Owners, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slote_id = models.ForeignKey(Slote, on_delete=models.CASCADE)
    payment = models.FloatField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'booking'