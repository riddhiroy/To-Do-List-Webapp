from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import ToDoList,Items
from .forms import CreateNewList
# Create your views here.
def index(request,id):
    t= ToDoList.objects.get(id=id)
    if t in request.user.todolist.all():
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in t.items_set.all():
                    if(request.POST.get ("c"+str(item.id))=='clicked'):
                        item.complete=True
                    else:
                        item.complete=False
                    item.save() 
            elif request.POST.get("newItem"):
                txt=request.POST.get("new")
                if len(txt)!=0:
                    t.items_set.create(text=txt, complete= False)
        return render(request,'list.html',{"t":t})
    else:
        return redirect('/')
  
def home(request):
    return render(request,'home.html',{})

def create(request):
    if(request.method=='POST'):
        form=CreateNewList(request.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            return redirect("/%i" % t.id)
    else:
        form= CreateNewList()
        return render(request, 'create.html',{"form":form})
def view(request):
    return render(request,'view.html',{})