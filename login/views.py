# login/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout




# Create your views here.

def loginRegister(request):
    return render (request, 'login/login.html') #Dirige a la plantilla login.html
