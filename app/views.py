from django.shortcuts import render
from django.http import HttpResponse as res
from Crypto.PublicKey import RSA
from django.http import request
from django import forms

class formlogin(forms.Form):
    email =forms.CharField(label = "Email", max_length=40, required=True,error_messages={'required':'khong duoc de trong'})
    passWord = forms.CharField(label= " Mật Khẩu", widget= forms.PasswordInput)
    
# Create your views here.
def index(request):
    form = formlogin()
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
        form = formlogin(request.POST)
        if form.is_valid():
            return res("login success"+ '  '+form.cleaned_data['email'])
    return res("login fail")
    #return res(request.POST.get("email"))