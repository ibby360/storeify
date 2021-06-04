from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    desctription = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='media', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("shop:product_by_category", args=[self.slug])
    

    def __str__(self):
        return self.category_name