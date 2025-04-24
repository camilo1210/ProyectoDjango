from django.db import models

class Proveedores(models.Model):
    idProvedor = models.AutoField(db_column='idProvedor', primary_key=True)
    nombreProvedor = models.CharField(db_column='nombreProvedor', max_length=45)
    direccion = models.CharField(db_column='direccion', max_length=45)
    telefono = models.CharField(db_column='telefono', max_length=45)
    

    class Meta:
        managed = False
        db_table = 'MateriaPrima'
