from django.shortcuts import render
from .models import Product

def home(request):
    return render(request,'catalog/home.html')


def contacts(request):
    return render(request,'catalog/contacts.html')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product_name': product.name,
        'product_price': product.price,
        'product_description': product.description,
        'product_category': product.category.name,
        'product_created_at': product.created_at,
        'product_updated_at': product.updated_at,
    }
    return render(request, 'catalog/product_detail.html', context)

def view_product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'catalog/products.html', context=context)
