from django.shortcuts import render

from productos.models import Product
# Create your views here.

def Tienda(request):

    productos=Product.objects.all()


    return render(request, "productos/Tienda.html", {"productos":productos})


