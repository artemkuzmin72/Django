from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

def home(request):
    return render(request,'catalog/home.html')


def contacts(request):
    return render(request,'catalog/contacts.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id' 

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'
