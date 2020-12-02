from django.urls import path,reverse,URLPattern

from . import views
app_name = 'sell'
urlpatterns = [
    path("",views.index,name = 'index'),
    
    path("show/<int:ID>",views.show, name = 'show'),  
    
]
