from django.db import models

class ConfiguracionSistema(models.Model):
    clave = models.CharField(max_length=100, unique=True, null=False)
    valor = models.TextField(null=False)
    def __str__(self): return self.clave
    class Meta: db_table = 'configuracion_sistema'