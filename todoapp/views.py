from django.shortcuts import render, redirect
from .forms import ToDoModelForm
from .models import ToDo

def index(request):
    form = ToDoModelForm()
    return render(request ,"todoapp/index.html", {"form": form })

def salom(request):
    if request.method == "POST":
        form = ToDoModelForm(request.POST)
        if form.is_valid():
            print("Form valid ekan")
            print("malumotlar :", form.cleaned_data["title"], form.cleaned_data["description"])
            ToDo.objects.create(title=form.cleaned_data["title"], description=form.cleaned_data["description"])
        else:
            print("form valid emas")
    return redirect("/")
    

def hayr(request):
    return render(request, "todoapp/hayr.html")