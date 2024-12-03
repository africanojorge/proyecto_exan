from django.shortcuts import render, redirect, get_object_or_404
from .models import OrdeneDeServicio 
from .forms import OrdenDeServicioForm
from django.contrib import messages

# Create your views here.

def lista_ordenes(request):
    ordenes = OrdeneDeServicio.objects.all()
    return render(request,'ordenes/lista_ordenes.html',{'ordenes':ordenes})

def detalle_orden(request, id):
    orden = get_object_or_404(OrdeneDeServicio, id=id)
    return render(request,'ordenes/detalle_orden.html',{'orden':orden})

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenDeServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Orden ha sido creada con éxito!')
            return redirect('ordenes:lista_ordenes')
    else:
        form = OrdenDeServicioForm()      
    return render(request,'ordenes/crear_orden.html', {'form':form})