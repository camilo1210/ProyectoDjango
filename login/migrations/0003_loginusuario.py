# Generated by Django 5.1.2 on 2024-11-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
