from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, default=99.99, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "123123"