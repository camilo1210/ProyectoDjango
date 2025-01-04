from django.shortcuts import render # type: ignore
from django.shortcuts import render# type: ignore
from django.http import HttpResponse# type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.contrib.auth import authenticate, login# type: ignore
from django.contrib import messages# type: ignore
from django.contrib.auth import logout# type: ignore
from .models import Usuario

# Create your views here.

def admin(request):
    return render(request, 'adminUsuarios/admin_user.html')  # Ruta al HTML de adminUsuarios

def home(request):
    return render(request, 'home/home.html')  # Ruta al HTML de home
