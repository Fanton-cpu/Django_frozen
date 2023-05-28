from django.db import models

# Create your models here.

class Product(models.Model):
    name_product = models.CharField(max_length=30)
    weight_ton = models.PositiveSmallIntegerField() 
    
    def __str__(self):
        return self.name_product