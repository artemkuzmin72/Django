from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from . import views

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('contacts/',contacts,name='contacts'),
    path('example',views.example_view,name='example'),
]