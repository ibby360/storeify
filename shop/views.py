from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Q 

# Create your views here.

def shop(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count':product_count
    }
    return render(request, 'shop/shop.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=product)

    except Exception as e:
        raise e
    
    context = {
        'product': product,
        'in_cart': in_cart
    }
    return render(request, 'shop/single-product.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            products = Product.objects.order_by('-created_date').filter(Q(product_name__icontains=q) | Q(description__icontains=q))
    
    context = {
        'products': products
    }
    return render(request, 'shop/shop.html', context)