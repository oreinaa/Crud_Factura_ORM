from django import forms
from .models import Cliente, Producto, Factura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'IVA'}
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')
        label = {'ruc': 'RUC', 'nombre': 'Nombre', 'direccion': 'Direccion', 'producto': 'Producto'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'total')
        label = {'cliente': 'Cliente', 'total': 'Total'}

