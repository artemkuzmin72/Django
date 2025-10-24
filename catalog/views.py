<<<<<<< HEAD
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
=======
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from .models import Product
from .forms import ProductForm


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')

>>>>>>> 0a3aaf5 (Access)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy("catalog:products")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Присваиваем владельца
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("Вы не можете редактировать этот продукт")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy("catalog:products")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("Вы не можете удалить этот продукт")
        return super().dispatch(request, *args, **kwargs)

@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, pk):
    """
    Позволяет пользователю с правом 'can_unpublish_product' отменить публикацию продукта.
    """
    product = get_object_or_404(Product, pk=pk)
    if not product.is_published:
        messages.info(request, f"Публикация продукта «{product.name}» уже отменена.")
    else:
        product.is_published = False
        product.save()
        messages.success(request, f"Публикация продукта «{product.name}» успешно отменена.")
    return redirect('catalog:products')
