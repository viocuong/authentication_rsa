from django.shortcuts import render
from django.http import HttpResponse as res,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return res("Hello da den voi trang ban hang")
def show(request, ID):
    return res(f"id cua ban la {ID}")
