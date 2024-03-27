from django.urls import path
from catalog.views import ContactView, ProductDetailView, ProductCreateView, ProductListView, PostCreateView, \
    PostUpdateView, PostListView, PostDetailView, PostDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('add-post/', PostCreateView.as_view(), name='add_post'),
    path('edit-post/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('delete-post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
]
