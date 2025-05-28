from django.db import models

# Create your models here.
class Proveedor(models.Model):
    idProvedor = models.AutoField(primary_key=True)
    nombreProvedor = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    class Meta:
        db_table = 'proveedor'  # <- Esto le dice a Django que use esta tabla exacta
        managed = False