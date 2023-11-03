from django.shortcuts import render
from import_excel_db.models import Inventory
# Create your views here.

def isel(request):
    listing = Inventory.objects.all()
    context = {
        'listing': listing
    }


    return render(request,'listing/table.html', context)




