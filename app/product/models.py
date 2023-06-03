from django.db import models

# Create your models here.

class Product(models.Model):
    name_product = models.CharField(max_length=30)
    weight_ton = models.PositiveSmallIntegerField() 
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.name_product, self.weight_ton)