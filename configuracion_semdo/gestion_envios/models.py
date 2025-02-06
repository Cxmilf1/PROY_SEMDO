from django.db import models
from gestion_facturas.models import Factura
from gestion_usuarios.models import Usuario

class EnvioFactura(models.Model):
    METODOS_ENVIO = [('Correo', 'Correo'), ('WhatsApp', 'WhatsApp'), ('Físico', 'Físico')]
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, db_column='id_factura')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    metodo_envio = models.CharField(max_length=50, choices=METODOS_ENVIO, null=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Envío {self.id} - {self.id_factura.id}"
    class Meta: db_table = 'envio_factura'