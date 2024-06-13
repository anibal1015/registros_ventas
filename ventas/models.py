from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User de Django
    documento = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.user.username  # Devuelve el nombre de usuario como representación del cliente

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre  # Devuelve el nombre del producto como representación del objeto

def validate_file_extension(value):
    if not value.name.endswith(('.pdf', '.doc', '.docx', '.png')):
        raise ValidationError('Solo se permiten archivos PDF, Word y PNG.')

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    archivos_adjuntos = models.FileField(upload_to='archivos_ventas/', validators=[validate_file_extension])

    def __str__(self):
        return f'{self.cliente.user.username} - {self.producto.nombre}'


class ArchivoAdjunto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='archivos_adjuntos')
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.archivo.name    