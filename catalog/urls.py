from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, ProductDetailView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='products'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('<int:pk>/blog/', BlogDetailView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]
