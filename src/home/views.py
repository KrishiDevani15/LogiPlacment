from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request, "views/homepage.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Your password is incorrect and confirm password are not same')
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,"views/signup.html")


def Login_process(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        
        
        user = authenticate(request,username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
            
            
        else:
            return HttpResponse('Username and Password are incorect')
    return render(request, "views/signup.html")

def hello(request):
    return render(request, "views/hello.html")

