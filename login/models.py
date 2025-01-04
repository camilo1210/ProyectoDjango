from django.db import models


class Materiaprima(models.Model):
    idmateriaprima = models.IntegerField(db_column='idMateriaPrima', primary_key=True)  # Field name made lowercase.
    
    nombremateriaprima = models.CharField(db_column='nombreMateriaPrima', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    costo = models.IntegerField(db_column='costo', blank=True, null=True)
    
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='proveedor', blank=True, null=True)
    
    cantidad = models.IntegerField(blank=True, null=True)
    
    unidadmedida = models.CharField(db_column='unidadMedida', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    categoria = models.CharField(db_column= 'categoria',max_length=45, blank=True, null=True)
    
    marca = models.CharField(db_column= 'marca',max_length=45, blank=True, null=True)
    
    fechallegada = models.DateTimeField(db_column='fechaLlegada', blank=True, null=True)  # Field name made lowercase.
    
    fechavencimiento = models.DateTimeField(db_column='fechaVencimiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MateriaPrima'


class MateriaPrimasAuditoria(models.Model):
    idmateriaprima = models.OneToOneField(Materiaprima, models.DO_NOTHING, db_column='idMateriaPrima', primary_key=True)  # Field name made lowercase.
    
    nombremateriaprimaanterior = models.CharField(db_column='nombreMateriaPrimaAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    costoanterior = models.IntegerField(db_column='costoAnterior', blank=True, null=True)  # Field name made lowercase.
    
    proveedoranterior = models.IntegerField(db_column='proveedorAnterior', blank=True, null=True)  # Field name made lowercase.
    
    cantidadanterior = models.IntegerField(db_column='cantidadAnterior', blank=True, null=True)  # Field name made lowercase.
    
    unidadmedidaanterior = models.CharField(db_column='unidadMedidaAnterior', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    categoriaanterior = models.CharField(db_column='categoriaAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    marcaanterior = models.CharField(db_column='marcaAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    fechallegadaanterior = models.DateTimeField(db_column='fechaLlegadaAnterior', blank=True, null=True)  # Field name made lowercase.
    
    fechavencimientoanterior = models.DateTimeField(db_column='fechaVencimientoAnterior', blank=True, null=True)  # Field name made lowercase.
    
    fechamodificacion = models.DateTimeField(db_column='fechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MateriaPrimaAuditoria'


class Materiaprima_has_Usuarios(models.Model):
    materiaprimaidmateriaprima = models.OneToOneField(Materiaprima, models.DO_NOTHING, db_column='MateriaPrimaIdMateriaPrima', primary_key=True)
    # Field name made lowercase. The composite primary key (MateriaPrimaIdMateriaPrima, Usuarios_idUsuarios) found, that is not supported. The first column is selected.
    
    usuarios_idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_idUsuarios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MateriaPrima_has_Usuarios'
        unique_together = (('materiaprimaidmateriaprima', 'usuarios_idusuarios'),)


class Proveedores(models.Model):
    idprovedor = models.IntegerField(db_column='idProvedor', primary_key=True)  # Field name made lowercase.
    
    nombreprovedor = models.CharField(db_column='nombreProvedor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    direccion = models.CharField(db_column='direccion',max_length=45, blank=True, null=True)
    
    telefono = models.CharField(db_column='telefono',max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proveedor'


class ProveedoresAuditoria(models.Model):
    idproveedorauditoria = models.OneToOneField(Proveedores, models.DO_NOTHING, db_column='idProveedorAuditoria', primary_key=True)  # Field name made lowercase.
    nombreanterior = models.CharField(db_column='nombreAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccionanterior = models.CharField(db_column='direccionAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonoanterior = models.IntegerField(db_column='telefonoAnterior', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProveedorAuditoria'


class Usuarios(models.Model):
    idusuarios = models.IntegerField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    
    usuario = models.CharField(db_column='usuario',max_length=45, blank=True, null=True)
    
    contrasenausuario = models.CharField(db_column='contrasenaUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    rol = models.CharField(db_column='rol',max_length=45, blank=True, null=True, default="usuario")
    
    email = models.CharField(db_column='email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.usuario



    class Meta:
        managed = False
        db_table = 'Usuarios'


class UsuariosAuditoria(models.Model):
    idusuario = models.OneToOneField(Usuarios, models.DO_NOTHING, db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    
    usuarioanterior = models.CharField(db_column='usuarioAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    contrasenausuarioanterior = models.CharField(db_column='contrasenaUsuarioAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    rolanterior = models.CharField(db_column='rolAnterior',max_length=45, blank=True, null=True)
    
    correoelectronicoanterior = models.CharField(db_column='emailAnterior', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    fechamodificacion = models.DateTimeField(db_column='fechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosAuditoria'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LoginUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    contraseña = models.CharField(max_length=45)  # Ajustar nombre
    email = models.CharField(max_length=45)      # Ajustar nombre
    usuario = models.CharField(max_length=45, null=True, blank=True)
    rol = models.CharField(max_length=50)         # Agregar este campo
    nombre = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'login_loginusuario'



class LoginProject(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login_project'


class LoginUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_usuario'

