from django.shortcuts import render
from django.http import HttpResponse as res
from Crypto.PublicKey import RSA

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def home(request):
    return res("home")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name
    })
