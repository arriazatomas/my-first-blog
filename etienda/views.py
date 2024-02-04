from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.

def productos(request):
    productos = Producto.objects.order_by('-category')
    return render(request, 'etienda/productos.html')

def producto_detallado(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'etienda/producto_detallado.html', {'producto': producto})

