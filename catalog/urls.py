from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from catalog.views import (
    home, contacts,
    ProductDetailView, ProductListView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    unpublish_product
)


app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),

    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('products/<int:pk>/unpublish/', unpublish_product, name='unpublish_product'),
    path('products/<int:pk>/publish/', views.publish_product, name='publish_product'),

    path('category/<int:category_id>/', views.products_by_category_view, name='products_by_category'),
]