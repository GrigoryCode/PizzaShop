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
    description = models.TextField(verbose_name='Description')
    price = models.FloatField(default=0, verbose_name='Price')
    image = models.ImageField('Image', upload_to='firstapp/photos', default='', blank=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
