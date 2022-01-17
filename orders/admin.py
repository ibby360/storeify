from django.contrib import admin
from orders.models import Order, OrderProduct, Payments

# Register your models here.
admin.site.register(Order)
admin.site.register(Payments)
admin.site.register(OrderProduct)