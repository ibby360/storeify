from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=False)
    trending_product = models.BooleanField(default=False)
    top_seller = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name