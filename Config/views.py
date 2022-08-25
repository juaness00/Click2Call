from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'Config/index.html')

def test(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            currentUser = User.objects.filter(username=username)
            if currentUser.filter(password=password).exists():
                return render(request,'Config/Success.html',{'form':username})
            else:
                messages.warning(request, 'Wrong password, try again.')
                form = UserForm()
                return render(request,'Config/test.html',{'form':form})
                
        else:
            messages.warning(request, 'Wrong username, try again.')
            form = UserForm()
            return render(request,'Config/test.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'Config/test.html',{'form':form})