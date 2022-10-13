from django.urls import path
from core.erp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
     
    path('Contacto', views.Contacto, name="Contacto"),
    path('Base', views.Base, name="Base"),
    path('Producto', views.Producto, name="Producto"),
    path('listaproductos', views.listaproductos, name="listaproductos"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
