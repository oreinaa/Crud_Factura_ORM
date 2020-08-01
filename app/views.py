from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, FacturaForm

def menu(request):  #Ese parametro siempre va
    opc = {'Menu': 'Menu Principal','producto': 'Productos', 'cliente':   #Diccionario
          'Clientes',  'factura': 'Facturas'}
    return render(request, 'principal.html', opc)

def producto(request):
     opc = {'Menu': 'Menu Principal', 'producto': 'Productos', 'cliente':   
          'Clientes', 'factura': 'Facturas'}
      
     if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()
                  return redirect('index')
     else:
            form = ProductoForm()
            opc ['form']= form

     return render(request, 'producto.html', opc)


def cliente(request):
      opc = {'Menu': 'Menu Principal', 'producto': 'Productos', 'cliente':   
          'Clientes', 'factura': 'Facturas'}

      if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()
                  return redirect('index')
      else:
            form = ClienteForm()
            opc ['form']= form
      return render(request, 'cliente.html', opc)

def factura(request):
      opc = {'Menu': 'Menu Principal', 'producto': 'Productos', 'cliente':   
          'Clientes', 'factura': 'Facturas'}

      if request.method == 'POST':
            form = FacturaForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()
                  return redirect('index')
      else:
            form = FacturaForm()
            opc ['form']= form
      return render(request, 'factura.html', opc)



