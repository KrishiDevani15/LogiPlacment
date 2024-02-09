from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "views/homepage.html")


def signup(request):
    return render(request, "views/signup.html")
