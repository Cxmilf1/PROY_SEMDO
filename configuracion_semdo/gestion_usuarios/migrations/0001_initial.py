# Generated by Django 5.1.6 on 2025-02-07 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
                ('id_rol', models.ForeignKey(db_column='id_rol', on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.rol')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
