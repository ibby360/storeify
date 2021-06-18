from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('categoty/<slug:category_slug>/', views.shop, name='product_by_category'), # Categoty view
    path('categoty/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), # Single product view
    path('search', views.search, name='search') # Search page view
]
