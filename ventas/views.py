from django.shortcuts import render, redirect
from .models import Venta, ArchivoAdjunto
from .forms import VentaForm

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardamos la venta y obtenemos una instancia del objeto
            venta = form.save()

            # Obtenemos la lista de archivos adjuntos desde el formulario
            archivos_adjuntos = request.FILES.getlist('archivos_adjuntos')

            # Recorremos la lista de archivos adjuntos y los asociamos a la venta
            for archivo in archivos_adjuntos:
                ArchivoAdjunto.objects.create(venta=venta, archivo=archivo)

            # Redireccionamos a la vista de lista de ventas después de guardar
            return redirect('lista_ventas')
    else:
        # Si es una solicitud GET (primera vez que se carga el formulario),
        # creamos una instancia del formulario vacío
        form = VentaForm()

    # Renderizamos la plantilla 'crear_venta.html' con el formulario apropiado
    return render(request, 'ventas/crear_venta.html', {'form': form})

def lista_ventas(request):
    # Obtenemos todas las ventas desde la base de datos
    ventas = Venta.objects.all()

    # Renderizamos la plantilla 'lista_ventas.html' con las ventas obtenidas
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})
