from django.http.response import HttpResponseRedirect
from app.models import User
from django.shortcuts import render
from django.urls import reverse
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
    if request.method== 'POST':
        form = FORMS.formRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(name=data['name'],phone=data['phone'],email = data['email'],passWord=data['passWord'])
            if user.email != User.objects.filter(email=user.email)['email']:
                user.save()
            else:
                return res("<script>alert('tai khoan da ton tai')</script>")
            
            return HttpResponseRedirect(reverse('app:index'))
        return
    form =FORMS.formRegister()
    return render(request,"app/register.html",{
        "form":form
    })
def login(request):
    if request.method == 'POST':
        form = FORMS.formLogin(request.POST)
        if form.is_valid():
            return res("login success"+ '  '+form.cleaned_data['email'])
    return render(request,'app/index.html',{'form':FORMS.formLogin()})
    #return res(request.POST.get("email"))