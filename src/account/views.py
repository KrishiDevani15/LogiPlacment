from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config = {
    "apiKey": "AIzaSyB5w2YhmM5hQxJlvEsjvdutuAlF9zN1pCY",
    "authDomain": "djangosignup-dff57.firebaseapp.com",
    "projectId": "djangosignup-dff57",
    "storageBucket": "djangosignup-dff57.appspot.com",
    "messagingSenderId": "242696560436",
    "appId": "1:242696560436:web:378d75f822c711da6c0f61",
    "measurementId": "G-9M8ZXE3Z8N",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signup(request):
    return render(request, "views/signup.html")


def postsignup(request):
    return HttpResponse("Hello World!")
