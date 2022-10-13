from django.shortcuts import render, HttpResponse

from productos.models import Product 


# Create your views here.

def Home(request):

    return render(request, "ProyectoWebApp/Home.html")

def Contacto(request):

    return render(request, "ProyectoWebApp/Contacto.html")

def Base(request):

    return render(request, "ProyectoWebApp/base.html")

def Producto(request):

    return render(request, "ProyectoWebApp/CompraProducto.html")    


def listaproductos(request):
    data = {
        'title': 'Productos',
        'Product': Product.objects.all(),
        'link': 'listaproductos',

    }
    return render(request, "admin/lista_productos.html", data)    
