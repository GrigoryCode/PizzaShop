from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    rating = models.FloatField(default=0, verbose_name='Rating')
    url = models.URLField(verbose_name='URL Adress')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Pizza Title')
    description = models.CharField(max_length=50, verbose_name='Short Description')
    price = models.IntegerField(default=0, verbose_name='Price')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
