from django.db import models

# Create your models here.
class Proveedor(models.Model):
    idProvedor = models.AutoField(primary_key=True)
    nombreProvedor = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    class Meta:
        db_table = 'Proveedores'  # <- Esto le dice a Django que use esta tabla exacta
        managed = False
class MateriaPrima(models.Model):
    idMateriaPrima = models.AutoField(primary_key=True)
    nombreMateriaPrima = models.CharField(max_length=45)
    costo = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, db_column='proveedor', on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    unidadMedida = models.CharField(max_length=10)
    categoria = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    fechaLlegada = models.DateTimeField()
    fechaVencimiento = models.DateTimeField()

    class Meta:
        db_table = 'MateriaPrima'
        managed = False  # Ya existe en la base de datos

    def __str__(self):
        return self.nombreMateriaPrima

