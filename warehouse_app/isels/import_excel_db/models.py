from django.db import models
from vendors.models import Vendors
# Create your models here.
 
shapes = [("مستطیل","مستطیل"),("استوانه","استوانه"), ("مربع","مربع"), ("دایره","دایره")]

class Inventory(models.Model):       
    part_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150,null=True)
    QTY = models.IntegerField()    
    length = models.IntegerField(null=True,blank=True)
    width = models.IntegerField(null=True,blank=True)
    depth = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    shape = models.CharField(choices= shapes, max_length=50, null=True)
    brand = models.CharField(max_length=50,null=True)
    coordinate = models.CharField(max_length=50, null=False) 
    def __str__(self):
        return self.name
    
    def Coordinate(self):
        return self.coordinate
                
    objects = models.Manager()

