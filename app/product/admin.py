from django.contrib import admin
from .models import Product, Client

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'coloreado', 'weight_ton')

#admin.site.register(Product)
#admin.site.register(Product, ProductAdmin)
    exclude = ('weight_ton',)

admin.site.register(Client) 


"""    
fieldsets = [
        (
            None,
            {
                "fields": ["name_product"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse", "wide", "extrapretty"],
                "fields": ["weight_ton"],
            },
        ),
    ]
"""

"""
def datos(self, obj):
    return obj.nombre.upper()
"""

"""
datos.short_description = "PRODUCTOS"
datos.empy_value_display = "???"
datos.admin_order_field = 'name_product"
"""



