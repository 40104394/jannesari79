from django.contrib import admin
from .models import part_form
class partformadmin(admin.ModelAdmin):

    list_display = ('lastname','part_type','manager', 'exact_model','qty')
    list_filter = ('exact_model',)
    search_fields = ('part_type', 'exact_model', 'lastname')

admin.site.register(part_form, partformadmin)
# Register your models here.
