from django.db import models

class CartItem(models.Model): 
      product_name = models.CharField(max_length=70)
      product_price = models.FloatField()
      product_quantity = models.PositiveIntegerField()

# Create your models here.
