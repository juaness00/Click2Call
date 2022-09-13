
from django.shortcuts import render, redirect
from .forms import ClientForm, UserForm, RegisterForm
from .models import User, Client
from django.contrib import messages
import requests
# Create your views here.
def index(request):
    return render(request, 'Config/error.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        contactInfo = request.POST['contactInfo']
        form = RegisterForm(request.POST)
        if len(username) > 0:
            if Client.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                form = RegisterForm()
                return render(request,'Config/Register.html',{'form':form})
            else:
                if Client.objects.filter(contactInfo=contactInfo).exists():
                    messages.warning(request, 'Email already exists')
                    form = RegisterForm()
                    return render(request,'Config/Register.html',{'form':form})
                elif form.is_valid():
                    form.save()
                    messages.warning(request, 'User Created Successfully')
                    response = redirect('http://127.0.0.1:8000/login/')
                    payload ={
                        "to": [contactInfo],
                        "subject": "User Created Successfully",
                        "text": "The user "+username+' was created sucessfully'
                    }
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'x-api-session-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjlWd0padGtkdzQ0WnpPSWdjcmpaUHFqWnFnRDBoMjJRR0ZpemgySHp2ZEs3WGFrZyIsImRlc2NyaXB0aW9uIjoianVhbmVzIiwiaWF0IjoxNjYyOTk2MzY0fQ.02tOpuu1Q47ZUC6DTBwE_0nqVp4VjTaSghdHnwGqvFI'
                    }
                    r = requests.post('http://165.227.180.82:8005/api/customer/comm/mail', json = payload, headers=headers)
                    print(r.text)
                    return response
                else:
                    return render(request, 'Config/error.html')
    else:
        form = RegisterForm()
        return render(request,'Config/Register.html',{'form':form})  

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            currentUser = User.objects.filter(username=username)
            if currentUser.filter(password=password).exists():
                request.session['username'] = username
                currentUser = request.session['username']
                request.session.modified = True
                context = {'username': currentUser}
                response = redirect('dashboard/',context)
                return response
            else:
                messages.warning(request, 'Wrong password, try again.')
                form = UserForm()
                return render(request,'Config/login.html',{'form':form})
                
        else:
            messages.warning(request, 'Wrong username, try again.')
            form = UserForm()
            return render(request,'Config/login.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'Config/login.html',{'form':form})

def dashboard(request):
    username = request.session['username']
    context = {'username':username}
    return render(request,'Config/Success.html',context)

def success(request):
    return render(request,'Config/SuccessfulChange.html')

def info(request):
    if request.method == 'POST':
        username = request.session['username']
        password = request.POST['password']
        contactInfo = request.POST['contactInfo']
        paymentNumber = request.POST['paymentNumber']

        currentUser = User.objects.get(username=username)
        currentClient = Client.objects.get(username=username)
        print(password, contactInfo, currentUser)
        if len(password) > 0:
            currentUser.password = password
        if len(contactInfo) > 0:
            currentClient.contactInfo = contactInfo
        if len(paymentNumber) > 0:
            currentClient.paymentNumber = paymentNumber
        currentUser.save()
        currentClient.save()
        messages.success(request, 'Profile details updated.')
        response = redirect('success/')
        return response
    else:
        form = ClientForm()
        username =request.session['username']
        context = {'form': form, 'username': username}
        return render(request,'Config/info.html', context)