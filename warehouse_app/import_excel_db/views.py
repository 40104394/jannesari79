from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Inventory
 
# Create your views here.
 
def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Inventory.objects.create(part_number=dbframe.part_number, name=dbframe.name, QTY=dbframe.qty,
            length=dbframe.length, width=dbframe.width, depth=dbframe.depth, weight=dbframe.weight,
            shape=dbframe.shape, brand = dbframe.Brand, coordinate=dbframe.coordinate)           
        return render(request, 'pages/upload_center.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'pages/upload_center.html',{})

