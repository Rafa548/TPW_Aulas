from django.shortcuts import render
from datetime import datetime
import json


# Create your views here.

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def login(request):
    tparams = {
        'title': 'Login',
        'message': 'Your login page.',
        'year': datetime.now().year,
    }
    return render(request, 'login.html', tparams)

def eurocv(request):
    f = open("app/static/eurocv.json", "r")
    data = json.load(f)
    return render(request, 'eurocv.html', data)

def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)
