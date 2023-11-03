from django.db import models
from datetime import datetime

class Isels(models.Model):
    
    isel_name = models.CharField(max_length=50)
    x_pos_cm = models.IntegerField()
    y_pos_cm = models.IntegerField()
    ori_degree = models.FloatField(max_length=6,)
    part_name = models.CharField(max_length=300,)
    list_update = models.DateTimeField(default=datetime.now, blank= True)

    def __str__(self):
        return self.isel_name
    
    def Coordinate(self):
        return self.isel_name
# Create your models here.
