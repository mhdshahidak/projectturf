from django.db import models

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
    status = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile/')
    bg_image = models.ImageField(upload_to='background/')
    first_image = models.ImageField(upload_to='turf/first')
    second_image = models.ImageField(upload_to='turf/second')
    third_image = models.ImageField(upload_to='turf/third')

    class Meta:
        db_table = 'owners'