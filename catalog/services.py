from .models import Product

def get_products_by_category(category_id):
    return Product.objects.filter(category__id=category_id, is_published=True).select_related('category', 'owner')