from django.db import models

class Materiaprima(models.Model):
    idMateriaPrima = models.AutoField(primary_key=True)
    nombreMateriaPrima = models.CharField(max_length=45)
    costo = models.IntegerField()
    proveedor = models.IntegerField()
    cantidad = models.IntegerField()
    unidadMedida = models.CharField(max_length=10)
    categoria = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    fechaLlegada = models.DateTimeField()
    fechaVencimiento = models.DateTimeField()

    class Meta:
        managed = False  # No se gestiona por Django
        db_table = 'MateriaPrima'