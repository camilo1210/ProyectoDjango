from django.db import models

# Create your models here.

#creo una tabla en la base de datos llamada Project
class Project(models.Model):
    name = models.CharField(max_length=20)