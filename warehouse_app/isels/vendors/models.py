from django.db import models

class Vendors(models.Model):
    vendor_name = models.CharField(max_length=50,)
    vendor_addres = models.TextField(max_length=500,)
    vendor_city = models.CharField(max_length=30,)
    vendor_state = models.CharField(max_length=30,)
    vendor_products = models.CharField(max_length=120,)
    vendor_phone_number = models.CharField(max_length=20,)
    def __str__(self):
        return self.vendor_name
    




# Create your models here.
