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
                request.session['username'] = username
                currentUser = request.session['username']
                request.session.modified = True
                context = {'username': currentUser}
                response = redirect('dashboard/',context)
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
    username = request.session['username']
    context = {'username':username}
    return render(request,'Config/Success.html',context)

def success(request):
    return render(request,'Config/SuccessfulChange.html')

def settings(request):
    if request.method == 'POST':
        username = request.session['username']
        password = request.POST['password']
        contactInfo = request.POST['contactInfo']
        paymentNumber = request.POST['paymentNumber']
        currentUser = User.objects.get(username=username)
        if len(password) > 0:
            currentUser.password = password
        if len(contactInfo) > 0:
            currentUser.contactInfo = contactInfo
        if len(paymentNumber) > 0:
            currentUser.paymentNumber = paymentNumber
        currentUser.save()
        messages.success(request, 'Profile details updated.')
        response = redirect('success/')
        return response
    else:
        form = ClientForm()
        username =request.session['username']
        context = {'form': form, 'username': username}
        return render(request,'Config/settings.html', context)