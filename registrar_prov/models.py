from django.db import models

class Proveedores(models.Model):
    idProvedor = models.AutoField(db_column='idProvedor',primary_key=True)
    nombreProvedor = models.CharField(db_column='nombreProvedor',max_length=255)
    direccion = models.CharField(db_column='direccion',max_length=255)
    telefono = models.CharField(db_column='telefono',max_length=20, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'Proveedores'

    def __str__(self):
        return self.nombreProvedor
