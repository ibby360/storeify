from django.contrib import admin
from shop.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'is_available',)
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)