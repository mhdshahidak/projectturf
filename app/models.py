from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    genter = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'customer'
