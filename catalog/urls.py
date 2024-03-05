from django.urls import path
from catalog.views import catalog_home, contacts

urlpatterns = [
    path('', catalog_home),
    path('contacts/', contacts),
]