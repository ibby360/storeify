from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.cat_remove, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.cat_remove_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout')

]

