from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .form import ProductoForm

# Create your views here.

def productos(request):
    productos = Producto.objects.order_by('-category')
    return render(request, 'etienda/productos.html')

def producto_detallado(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'etienda/producto_detallado.html', {'producto': producto})

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.author = request.user
            producto.save()
            return redirect('producto_detallado', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'etienda/producto_nuevo.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.author = request.user
            producto.save()
            return redirect('producto_detallado', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'etienda/producto_editar.html', {'form': form})

