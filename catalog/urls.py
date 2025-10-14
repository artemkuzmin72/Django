from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, view_product, product_detail
app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/',contacts,name='contacts'),
    path('products/',view_product,name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]