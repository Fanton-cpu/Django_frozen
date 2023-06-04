# from django.http import HttpResponse
from typing import Any, Dict
# from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product

# Create your views here.

def home(request):
   # return HttpResponse("<h1>Hello world!</h1>")
   productList =Product.objects.all()
   data = {
      'titulo': 'Gestión de productos',
      'product': productList
   }
   # return render(request, "gestionProduct.html", {"product": productList})
   return render(request, "gestionProduct.html", data)

class ProductListView(ListView):
   model = Product
   template_name = "gestionProduct.html"
   
   def get_queryset(self):
      return Product.objects.all()
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['titulo'] = 'Gestión de productos'
      # print(context)
      return context

def eliminar_producto(request,id):
   producto = Product.objects.get(id=id)
   producto.delete()
   
   return redirect('/')