from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hello world')

    return render(request,'home.html'),

def home(request):
    # return HttpResponse('home')
    
   return render(request,'about.html')

