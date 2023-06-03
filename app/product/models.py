from django.db import models
from django.utils.html import format_html
from .choice import gender

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    company = models.CharField(max_length=20, verbose_name='Company')
    birthdate = models.DateField(verbose_name='Birthdate')
    gender = models.CharField(max_length=1, choices=gender, default='F')
    
    def name_complete(self):
        return "{} {}, {}".format(self.name,self.last_name, self.company)

    def __str__(self):
        return self.name_complete
    
    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisores'
        db_table = 'supervisor'
        ordering = ['name','-last_name']

class Product(models.Model):
    name_product = models.CharField(max_length=30)
    weight_ton = models.PositiveSmallIntegerField()
    supervisor = models.ForeignKey(Client,null=True,blank=True,on_delete=models.CASCADE) 
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.name_product, self.weight_ton)
    
    def coloreado(self):
        if self.weight_ton >= 15:
            return format_html('<span style="color: blue;">{0}</span>'.format(self.name_product))
        else:
            return format_html('<span style="color: red;">{0}</span>'.format(self.name_product))
        
    
    
    
    
    