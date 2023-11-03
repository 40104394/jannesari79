from django.db import models
from vendors.models import Vendors
from import_excel_db.models import Inventory
shapes = [("مستطیل","مستطیل"),("استوانه","استوانه"), ("مربع","مربع"), ("دایره","دایره")]
parts_type = [("buy","خرید"), ("produce","تولیدی")]
class parts(models.Model):
    part_num = models.IntegerField()
    part_name = models.CharField(max_length=50,)
    length = models.FloatField(max_length=20,)
    width = models.FloatField(max_length=20,)
    depth = models.FloatField(max_length=20,)
    shape = models.CharField(choices=shapes,)
    vendors = models.ForeignKey(Vendors, on_delete=models.DO_NOTHING)
    type = models.CharField(choices=parts_type,)
    qty = models.IntegerField()
    #inventory = models.ForeignKey(Inventory.part_number, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.part_name
# Create your models here.
