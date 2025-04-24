
from django.db import models

class MateriaPrima(models.Model):
    idmateriaprima = models.AutoField(db_column='idMateriaPrima', primary_key=True)
    nombreMateriaPrima = models.CharField(db_column='nombreMateriaPrima', max_length=45)
    costo = models.IntegerField()
    proveedor = models.ForeignKey('registrar_prov.Proveedores', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    unidadMedida = models.CharField(db_column='unidadMedida', max_length=10)
    categoria = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    fechaLlegada = models.DateTimeField(db_column='fechaLlegada')
    fechaVencimiento = models.DateTimeField(db_column='fechaVencimiento')

    class Meta:
        managed = False
        db_table = 'MateriaPrima'
        

