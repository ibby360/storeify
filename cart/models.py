from django.db import models
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product
