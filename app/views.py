from django.shortcuts import render
from django.http import HttpResponse as res,HttpResponseRedirect as redirect
from Crypto.PublicKey import RSA
from django.http import request
from app.forms import FORMS

# Create your views here.
def index(request):
    form = FORMS.formLogin()
    return render(request, "app/index.html",{
        "form":form
    })


def home(request):
    return res("home")
def greet(request, name):
    return render(request, "app/greet.html", {
        "name": name
    })
    
def register(request):
    return res("welcom register")
def login(request):
    if request.method == 'POST':
        form = FORMS.formLogin(request.POST)
        if form.is_valid():
            return res("login success"+ '  '+form.cleaned_data['email'])
    return render(request,'app/index.html',{'form':FORMS.formLogin()})
    #return res(request.POST.get("email"))