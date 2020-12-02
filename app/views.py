from django.http.response import HttpResponseRedirect
from app.models import PublicKey, User
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse as res,HttpResponseRedirect as redirect
from Crypto.PublicKey import RSA
from django.http import request
from app.forms import FORMS
from app.function import *
import mimetypes

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
            ##################3
            sizePublickey = len(PublicKey.objects.all())+1
            sizeUser = len(User.objects.all())+1
            n, e, d = generateKey()
            userid = generateId(sizeUser)
            
            idpublickey = generateId(sizePublickey)
            publicKey = PublicKey(idPublicKey = str(idpublickey), publicKeyE = str(e), publicKeyN = str(n))
            user = User(userId = userid, name = data['name'], phone = data['phone'], email = data['email'])
            #Id + id khoa cong khai
            CI =  str(encode(userid, n, d))+'#'+str(idpublickey)

            f = open('./file/'+data['email']+'.txt','w')
            f.write(CI) 
            f.close()
            return HttpResponseRedirect(f"/download/{data['email']}")
            C = int(str(CI).split('#')[0])
            P = decode(C,n,e)

            return res(P == int.from_bytes(sha512(str(userid).encode()).digest(),byteorder='big')) 
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
def download_file(request,file_name):
    fl_path = 'file/'
    filename = file_name+'.txt'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = res(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
def home(request):
    return res("dang nhap thanh cong")
def success(request):
    return res("dang ky ok ")