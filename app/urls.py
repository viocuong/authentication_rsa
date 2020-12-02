from django.urls import path
from . import views
app_name="app"
urlpatterns=[
    path("",views.index,name='index'),
    #path("<str:name>",views.greet,name="greet"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("home/",views.home,name="home"),
    path("register/success", views.success, name= "success"),
    path("download/<str:file_name>/",views.download_file, name="download")
]