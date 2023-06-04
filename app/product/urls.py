from django.urls import path
from app.product.views import ProductListView, eliminar_producto

urlpatterns = [
    path('', ProductListView.as_view(), name = 'gestion_producto'),
    path('eliminacionProducto/<int:id>',eliminar_producto),
]