from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "precio", "stock")
    search_fields = ("nombre",)
    list_filter = ()
    ordering = ("nombre", "stock")

admin.site.register(model_or_iterable=Producto, admin_class=ProductoAdmin)  