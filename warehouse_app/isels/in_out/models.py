from django.db import models
from parts.models import parts
import datetime
d = datetime.datetime.now()
parts_type = [("1","مته"),("2","انگشتی"),("3","مرغک"),("4","برقو")]

class part_form(models.Model):  
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    part_type = models.CharField(choices=parts_type)
    exact_model = models.CharField(max_length=50)
    partnumber = models.ForeignKey(parts, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()

# Create your models here.
