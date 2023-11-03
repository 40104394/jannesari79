from django.shortcuts import render,redirect
from .forms import parts_form
from .models import part_form
from .choices import type_choices

def In(request):
    
    
    context={
        'type_choices':type_choices,
     }
    
    if request.method == "POST": 
        form = parts_form(request.POST) 
        if form.is_valid(): 
            obj = part_form()
            obj.firstname=request.POST.get['firstname']
            obj.lastname=request.POST.get['lastname']
            obj.manager =request.POST.get['manager']
            obj.part_type=request.POST.get['part_type']
            obj.exact_model=request.POST.get['exact_model']
            obj.partnumber=request.POST.get['partnumber']
            obj.qty=request.POST.get['qty']
            obj.save()
            try:
                return redirect('/')  
            except:
                pass
    else:
         
        form = parts_form()  
    return render(request,'pages/input.html',context) 


    
def Out(request):
    if request.method == "POST":  
        form = parts_form(request.POST)  
        if form.is_valid():
            form.save()  

            try: 
             
 
                return redirect('/')  
            except:  
                pass  
    else:
        form = parts_form()  
    return render(request,'pages/out.html',{'form':form}) 


