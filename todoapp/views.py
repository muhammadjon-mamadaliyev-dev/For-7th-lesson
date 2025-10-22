
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoModelForm

# Create your views here.

def index(request):
    todos =  Todo.objects.all()
    return render(request,'todoapp/index.html',{'todos':todos})

def create_todo(request):
    form = TodoModelForm()
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render   (request,'todoapp/todo_create.html',{'form':form})
    return render   (request,'todoapp/todo_create.html',{'form':form}) 

def todo_item(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'todoapp/todo_items.html',{"todo":todo})

def delete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('home')  

def edit(request,pk):
    todo = Todo.objects.get(id = pk)

    if  request.method == "POST":
       form = TodoModelForm(request.POST, instance = todo)
       if form.is_valid(): 
          form.save()
          return redirect('home')
       
    return render(request,"todoapp/edit.html",{"todo":todo})
        
