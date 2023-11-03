from django.contrib import admin
from .models import Inventory

class PartsINAdmin(admin.ModelAdmin):
    list_display = ('part_number','name','QTY', 'length','width','coordinate')
    list_filter = ('coordinate',)
    search_fields = ('name', 'coordinate', 'part_number')


admin.site.register(Inventory, PartsINAdmin)
# Register your models here.
