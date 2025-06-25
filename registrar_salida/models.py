from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        managed = False  # No queremos que Django cree/modifique esta tabla
        db_table = 'producto'

class Salida(models.Model):
    fecha = models.DateTimeField()
    productos = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=255)
    materias_primas = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'salida'  # Esto indica que usaremos una tabla ya existente en la base de datos

    def __str__(self):
        return f"Salida del {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"

