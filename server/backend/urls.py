from django.urls import path,re_path
#from django.conf.urls import  url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('id', views.projectid, name='home'),
    path('name', views.projectname, name='home'),

]