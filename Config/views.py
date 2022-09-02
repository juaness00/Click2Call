from django.shortcuts import render, redirect
from .forms import ClientForm, UserForm
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
                response = redirect('dashboard/',{'formUsername': username})
                return response
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

def dashboard(request):
    return render(request,'Config/Success.html')

def success(request):
    return render(request,'Config/SuccessfulChange.html')

def settings(request):
    if request.method == 'POST':
        username = User.objects.get(username='Juanes')
        password = request.POST['password']
        contactInfo = request.POST['contactInfo']
        currentUser = User.objects.get(username=username)
        currentUser.password = password
        currentUser.contactInfo = contactInfo
        currentUser.save()
        messages.success(request, 'Profile details updated.')
        response = redirect('success/')
        return response
    else:
        form = ClientForm()
        username = User.objects.get(username='Juanes')
        return render(request,'Config/settings.html', {'form': form,'formUsername': username})