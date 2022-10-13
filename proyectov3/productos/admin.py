from django.contrib import admin

from productos.models import Product,Client,Sale,DetSale,Tallas
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("name","color")
    search_fields = ("name","color")
    list_filter = ("color",)

class TallasAdmin(admin.ModelAdmin):
    list_display = ("nam","talla","cant")
    search_fields = ("nam","talla")
    list_filter = ("talla",)    
    
class SaleAdmin(admin.ModelAdmin):
    list_display = ("cli","total")
    list_filter=("date_joined",)   
    date_hierarchy="date_joined"

admin.site.register(Product, ProductosAdmin)
admin.site.register(Client)
admin.site.register(Sale, SaleAdmin)
admin.site.register(DetSale)
admin.site.register(Tallas, TallasAdmin)

