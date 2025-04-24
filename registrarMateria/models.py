
from django.db import models

class MateriaPrima(models.Model):
    idmateriaprima = models.AutoField(db_column='idMateriaPrima', primary_key=True)
    nombremateriapri = models.CharField(db_column='nombreMateriaPri', max_length=45)
    costo = models.IntegerField()
    proveedor = models.IntegerField()
    cantidad = models.IntegerField()
    unidadmedida = models.CharField(db_column='unidadMedida', max_length=10)
    categoria = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    fechallegada = models.DateTimeField(db_column='fechaLlegada')
    fechavencimiento = models.DateTimeField(db_column='fechaVencimiento')

    class Meta:
        managed = False
        db_table = 'MateriaPrima'
