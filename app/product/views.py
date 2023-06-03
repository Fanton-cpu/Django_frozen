# from django.http import HttpResponse
from django.shortcuts import render
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
