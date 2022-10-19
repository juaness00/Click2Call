from django.utils import translation
from django.shortcuts import render, redirect
from .forms import ClientForm, UserForm, RegisterForm, MovieForm
from .models import User, Client
from django.contrib import messages
import requests
from urllib.request import urlopen
import json
import ssl
from django.db import transaction

ssl._create_default_https_context = ssl._create_unverified_context

# Create your views here.
def index(request):
    return render(request, 'Config/error.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        contactInfo = request.POST['contactInfo']
        form = RegisterForm(request.POST)
        print(request.POST['language'])
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
            currentUser = User.objects.get(username=username)

            if currentUser.password == password:
                request.session['username'] = username
                request.session['language'] = currentUser.language
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
    translation.activate(request.session['language'])
    context = {'username':username}
    return render(request,'Config/Success.html',context)

def success(request):
    translation.activate(request.session['language'])
    return render(request,'Config/SuccessfulChange.html')

def info(request):
    translation.activate(request.session['language'])
    if request.method == 'POST':
        username = request.session['username']
        password = request.POST['password']
        contactInfo = request.POST['contactInfo']
        paymentNumber = request.POST['paymentNumber']
        language = request.POST['language']
        print(language)
        currentClient = Client.objects.get(username=username)
        print(password, contactInfo, currentClient.language, language)
        if len(password) > 0:
            currentClient.password = password
        if len(contactInfo) > 0:
            currentClient.contactInfo = contactInfo
        if len(paymentNumber) > 0:
            currentClient.paymentNumber = paymentNumber
        if len(language) > 0:
            currentClient.language = language
            print(currentClient.language)
        currentClient.save()
        print(Client.objects.get(username=username).language)
        request.session['language'] = currentClient.language
        request.session.modified = True
        messages.success(request, 'Profile details updated.')
        response = redirect('success/')
        return response
    else:
        form = ClientForm()
        username =request.session['username']
        context = {'form': form, 'username': username}
        return render(request,'Config/info.html', context)

def movie(request):
    translation.activate(request.session['language'])
    if request.method == 'POST':
        username = request.session['username']
        favoriteMovie = request.POST['Favorite Movie']
        print(favoriteMovie, username)
        currentClient = Client.objects.get(username=username)
        if currentClient.favoriteMovie != favoriteMovie:
            currentClient.favoriteMovie = favoriteMovie
            currentClient.save()
            url = 'https://swapi.dev/api/films'
            response = urlopen(url)
            data_json = json.loads(response.read())
            films = data_json['results']
            for film in films:
                if film['title'] == favoriteMovie:
                    url = film['url']
            response = urlopen(url)
            data_json = json.loads(response.read()) 
            title = data_json['title']
            for item in title:
                openingCrawl = film['opening_crawl']
                director = film['director']
                producer = film['producer']
                releaseDate = film['release_date']
            context={
                'title': title,
                "openingCrawl": openingCrawl,
                'director': director,
                'producer': producer,
                'releaseDate': releaseDate
            }
            return render(request,'config/movieDetails.html',context)
    else:
        username = request.session['username']
        currentClient = Client.objects.get(username=username)
        favoriteMovie = currentClient.favoriteMovie
        print(favoriteMovie, username)
        if currentClient.favoriteMovie != None:
            url = 'https://swapi.dev/api/films'
            response = urlopen(url)
            data_json = json.loads(response.read())
            films = data_json['results']
            for film in films:
                    if film['title'] == favoriteMovie:
                        url = film['url']
            response = urlopen(url)
            data_json = json.loads(response.read())
            film = data_json
            title = film['title']
            for item in title:
                openingCrawl = film['opening_crawl']
                director = film['director']
                producer = film['producer']
                releaseDate = film['release_date']
            context={
                'title': title,
                "openingCrawl": openingCrawl,
                'director': director,
                'producer': producer,
                'releaseDate': releaseDate
            }
            return render(request,'config/movieDetails.html',context)
        else:
            form = MovieForm()
            url = 'https://swapi.dev/api/films'
            response = urlopen(url)
            data_json = json.loads(response.read())
            films = data_json['results']
            titles=[]
            for film in films:
                titles.append(film['title'])
            print(titles)
            context = {'form': form,'titles':titles}
            return render(request, 'Config/movieChange.html',context)


def movieChange(request):
    translation.activate(request.session['language'])
    if request.method == 'POST':
        username = request.session['username']
        favoriteMovie = request.POST['Favorite Movie']
        print(favoriteMovie, username)
        currentClient = Client.objects.get(username=username)
        currentClient.favoriteMovie = favoriteMovie
        currentClient.save()
        url = 'https://swapi.dev/api/films'
        response = urlopen(url)
        data_json = json.loads(response.read())
        films = data_json['results']
        for film in films:
            if film['title'] == favoriteMovie:
                url = film['url']
        response = urlopen(url)
        data_json = json.loads(response.read())
        film = data_json
        title = film['title']
        for item in title:
            openingCrawl = film['opening_crawl']
            director = film['director']
            producer = film['producer']
            releaseDate = film['release_date']
        context={
            'title': title,
            "openingCrawl": openingCrawl,
            'director': director,
            'producer': producer,
            'releaseDate': releaseDate
        }
        return redirect('http://127.0.0.1:8000/login/dashboard/movie/',context)
    else:
        form = MovieForm()
        url = 'https://swapi.dev/api/films'
        response = urlopen(url)
        data_json = json.loads(response.read())
        films = data_json['results']
        titles=[]
        for film in films:
            titles.append(film['title'])
        print(titles)
        context = {'form': form,'titles':titles}
        return render(request, 'Config/movieChange.html',context)