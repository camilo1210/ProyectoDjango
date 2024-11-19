# Generated by Django 5.1.3 on 2024-11-19 23:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LoginLoginusuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login_loginusuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materiaprima',
            fields=[
                ('idmateriaprima', models.IntegerField(db_column='idMateriaPrima', primary_key=True, serialize=False)),
                ('nombremateriaprima', models.CharField(blank=True, db_column='nombreMateriaPrima', max_length=45, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('unidadmedida', models.CharField(blank=True, db_column='unidadMedida', max_length=10, null=True)),
                ('categoria', models.CharField(blank=True, max_length=45, null=True)),
                ('marca', models.CharField(blank=True, max_length=45, null=True)),
                ('fechallegada', models.DateTimeField(blank=True, db_column='fechaLlegada', null=True)),
                ('fechavencimiento', models.DateTimeField(blank=True, db_column='fechaVencimiento', null=True)),
            ],
            options={
                'db_table': 'MateriaPrima',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idprovedor', models.IntegerField(db_column='idProvedor', primary_key=True, serialize=False)),
                ('nombreprovedor', models.CharField(blank=True, db_column='nombreProvedor', max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idusuarios', models.IntegerField(db_column='idUsuarios', primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=45, null=True)),
                ('contrasenausuario', models.CharField(blank=True, db_column='contrasenaUsuario', max_length=45, null=True)),
                ('rol', models.CharField(blank=True, max_length=45, null=True)),
                ('correoelectronico', models.CharField(blank=True, db_column='correoElectronico', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materiaprimaauditoria',
            fields=[
                ('idmateriaprima', models.OneToOneField(db_column='idMateriaPrima', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventario.materiaprima')),
                ('nombremateriaprimaanterior', models.CharField(blank=True, db_column='nombreMateriaPrimaAnterior', max_length=45, null=True)),
                ('costoanterior', models.IntegerField(blank=True, db_column='costoAnterior', null=True)),
                ('proveedoranterior', models.IntegerField(blank=True, db_column='proveedorAnterior', null=True)),
                ('cantidadanterior', models.IntegerField(blank=True, db_column='cantidadAnterior', null=True)),
                ('unidadmedidaanterior', models.CharField(blank=True, db_column='unidadMedidaAnterior', max_length=10, null=True)),
                ('categoriaanterior', models.CharField(blank=True, db_column='categoriaAnterior', max_length=45, null=True)),
                ('marcaanterior', models.CharField(blank=True, db_column='marcaAnterior', max_length=45, null=True)),
                ('fechallegadaanterior', models.DateTimeField(blank=True, db_column='fechaLlegadaAnterior', null=True)),
                ('fechavencimientoanterior', models.DateTimeField(blank=True, db_column='fechaVencimientoAnterior', null=True)),
                ('fechamodificacion', models.DateTimeField(blank=True, db_column='fechaModificacion', null=True)),
            ],
            options={
                'db_table': 'MateriaPrimaAuditoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MateriaprimaHasUsuarios',
            fields=[
                ('materiaprimaidmateriaprima', models.OneToOneField(db_column='MateriaPrimaIdMateriaPrima', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventario.materiaprima')),
            ],
            options={
                'db_table': 'MateriaPrima_has_Usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedorauditoria',
            fields=[
                ('idproveedorauditoria', models.OneToOneField(db_column='idProveedorAuditoria', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventario.proveedor')),
                ('nombreanterior', models.CharField(blank=True, db_column='nombreAnterior', max_length=45, null=True)),
                ('direccionanterior', models.CharField(blank=True, db_column='direccionAnterior', max_length=45, null=True)),
                ('telefonoanterior', models.IntegerField(blank=True, db_column='telefonoAnterior', null=True)),
            ],
            options={
                'db_table': 'ProveedorAuditoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuariosauditoria',
            fields=[
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventario.usuarios')),
                ('usuarioanterior', models.CharField(blank=True, db_column='usuarioAnterior', max_length=45, null=True)),
                ('contrasenausuarioanterior', models.CharField(blank=True, db_column='contrasenaUsuarioAnterior', max_length=45, null=True)),
                ('rol', models.CharField(blank=True, max_length=45, null=True)),
                ('correoelectronico', models.CharField(blank=True, db_column='correoElectronico', max_length=45, null=True)),
                ('fechamodificacion', models.DateTimeField(blank=True, db_column='fechaModificacion', null=True)),
            ],
            options={
                'db_table': 'UsuariosAuditoria',
                'managed': False,
            },
        ),
    ]
