from django.urls import path
from catalog.views import catalog_home, contacts, product, add_product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
    path('add-product/', add_product, name='add_product'),
]