from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from .models import Product, Category
from .forms import ProductForm
from .services import get_products_by_category
from django.core.cache import cache


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


def products_by_category_view(request, category_id):
    """
    Отображает список продуктов по категории
    """
    category = get_object_or_404(Category, id=category_id)
    products = get_products_by_category(category.id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'catalog/products_by_category.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)  
        return queryset


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


@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def publish_product(request, pk):
    """
    Позволяет пользователю с правом 'can_unpublish_product' повторно публиковать продукт.
    """
    product = get_object_or_404(Product, pk=pk)
    if product.is_published:
        messages.info(request, f"Продукт «{product.name}» уже опубликован.")
    else:
        product.is_published = True
        product.save()
        messages.success(request, f"Продукт «{product.name}» успешно опубликован.")
    return redirect('catalog:products')