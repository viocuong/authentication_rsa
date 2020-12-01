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
def greet(request, name): 
    return render(request, "app/greet.html", {
        "name": name
    })
def register(request):
    if request.method== 'POST':
        form = FORMS.formRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(name=data['name'],phone=data['phone'],email = data['email'])
            try:
                u =User.objects.filter(email=user.email).get().email
                if ( u == user.name): return res("<script>alert('tai khoan da ton tai')</script>")
            except User.DoesNotExist:
                user.save()
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
            ins = form.cleaned_data
            if User.objects.filter(email = ins['email'], passWord= ins['passWord']).exists()== True:
                return HttpResponseRedirect(reverse("app:home"))    
    return render(request,'app/index.html',{'form':FORMS.formLogin()})
    #return res(request.POST.get("email"))
def home(request):
    return res("dang nhap thanh cong")
def success(request):
    return res("dang ky ok ")