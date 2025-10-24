from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm 

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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy("catalog:products")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm 
    template_name = 'catalog/product_update.html'
    pk_url_kwarg = 'product_id' 

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    pk_url_kwarg = 'product_id' 
    success_url = reverse_lazy("catalog:products")