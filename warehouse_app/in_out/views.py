from django.shortcuts import render
from .forms import parts_form
from .models import part_form
def In(request):
    if request.method == "POST":  
        form = parts_form(request.POST)  
        
        if form.is_valid():
            form.save()
            try:  
                form.save()

                return redirect('/')  
            except:  
                pass  
    else:
         
        form = parts_form()  
    return render(request,'pages/input.html',{'form':form})  


    
def Out(request):
    if request.method == "POST":  
        form = parts_form(request.POST)  
        if form.is_valid():
            form.save()  

            try: 
                form.save()
 
                return redirect('/')  
            except:  
                pass  
    else:
        form = parts_form()  
    return render(request,'pages/out.html',{'form':form}) 


