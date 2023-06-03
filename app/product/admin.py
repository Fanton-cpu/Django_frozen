from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Product)
#admin.site.register(Product, ProductAdmin)