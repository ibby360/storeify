from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
    trending_products = Product.objects.filter(trending_product=True, is_available=True)
    top_sellers = Product.objects.filter(top_seller=True, is_available=True)
    featured = Product.objects.filter(featured=True, is_available=True)[:3]

    context = {
        'trending_products': trending_products,
        'top_sellers': top_sellers,
        'featured': featured
    }
    return render(request, 'index.html', context)