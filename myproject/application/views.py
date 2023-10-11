from django.shortcuts import render
#  from django.http import HttpResponse

def index_copy(request):
    return render(request,'index copy.html')
