from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'producto'  # nombre exacto de la tabla en la base de datos
        managed = False  
