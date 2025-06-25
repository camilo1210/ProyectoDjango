from django.http import HttpResponse# type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.contrib.auth import authenticate, login# type: ignore
from django.contrib import messages# type: ignore
from django.contrib.auth import logout# type: ignore
from .models import Usuario
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def admin(request):
    return render(request, 'adminUsuarios/admin_user.html')  # Ruta al HTML de adminUsuarios

def home(request):
    return render(request, 'home/home.html')  # Ruta al HTML de home
def get_usernames(request):
    usuarios = User.objects.all()
    data = [{"name": user.username} for user in usuarios]
    return JsonResponse(data, safe=False)
@csrf_exempt
def delete_user(request):
    if request.method == "DELETE":
        try:
            body = json.loads(request.body)
            username = body.get("username")

            user = User.objects.get(username=username)
            user.delete()
            return JsonResponse({"message": "Usuario eliminado correctamente"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
@csrf_exempt
def update_user(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            old_username = data.get('old_username')
            new_username = data.get('new_username')
            new_first_name = data.get('new_first_name')

            user = User.objects.get(username=old_username)
            user.username = new_username
            user.first_name = new_first_name
            user.save()

            return JsonResponse({'message': 'Usuario actualizado correctamente'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)