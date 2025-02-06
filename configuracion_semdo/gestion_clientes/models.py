from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, unique=True)
    def __str__(self): return self.nombre
    class Meta: db_table = 'cliente'