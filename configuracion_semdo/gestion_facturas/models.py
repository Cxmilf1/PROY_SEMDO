from django.db import models
from gestion_clientes.models import Cliente

class Factura(models.Model):
    ESTADOS = [('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Vencido', 'Vencido')]
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    fecha_emision = models.DateField(null=False)
    fecha_vencimiento = models.DateField(null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente', null=False)
    archivo_pdf = models.CharField(max_length=255, null=False)
    def __str__(self): return f"Factura {self.id} - {self.id_cliente.nombre}"
    class Meta: db_table = 'factura'
