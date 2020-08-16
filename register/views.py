from django.shortcuts import render,redirect
from .forms import RegistrationForm
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            return redirect('/')
        else:
            form=RegistrationForm()
    else:
            form=RegistrationForm()
    return render(request,'register.html',{"form":form})