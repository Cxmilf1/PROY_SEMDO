from django.db import models

from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    def __str__(self): return self.nombre
    class Meta: db_table = 'rol'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=150, unique=True, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol')
    def __str__(self): return self.nombre
    class Meta: db_table = 'usuario'
