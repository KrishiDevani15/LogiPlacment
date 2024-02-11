from django.contrib import admin
from django.urls import path
from home.views import *
from . import views
urlpatterns = [
    path("", views.home,name="home"),
    path("hello/", views.hello, name="hello"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.Login_process, name="login"),
]
