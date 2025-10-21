from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/',contacts, name='contacts'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]