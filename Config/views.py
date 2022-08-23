from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
#from .forms import clientForm
# Create your views here.
def index(request):
    return render(request, 'Config/index.html')

def test(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'Config/test.html', context)
