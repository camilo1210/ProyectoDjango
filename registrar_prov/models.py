from django.db import models

class Proveedores(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'Proveedores'  # Nombre de la tabla en la base de datos