from category.models import Category

def cat_links(request):
    categories = Category.objects.all()

    return dict(categories=categories)