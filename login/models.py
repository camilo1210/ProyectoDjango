from django.db import models

# Create your models here.

#creo una tabla en la base de datos llamada Project
class Project(models.Model):
    name = models.CharField(max_length=20)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

