from django.shortcuts import render
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm,TodoupdateForm

person={'name':'zari'}

def articles(request):
    all=Todo.objects.all()
    return render(request,'home.html',{'all':all})


def articles_list(request):
    return render(request ,'about.html',context=person)


def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})

def create(request):
    if request.method =='POST':
      form = TodoCreateForm(request.POST)
      if form.is_valid():
       cd=form.cleaned_data
       Todo.objects.create(title=cd['title'],body=cd['body'],created=cd['created'])
       messages.success(request,'Todo created successfily','success')
       return redirect('home')
    else:
     form = TodoCreateForm()
    return render (request,'create.html',{'form':form})

def update(request,todo_id):
   todo=Todo.objects.get(id=todo_id)
   if request.method=='POST':
      form=TodoupdateForm(request.POST,instance=todo)
      if form.is_valid():
         form.save()
         messages.sucess(request,'your todo updated successfully','success')
         return redirect('details',todo_id)
   else:
      form=TodoupdateForm(instance=todo)
   return render (request,'update.html',{'form':form})
   
