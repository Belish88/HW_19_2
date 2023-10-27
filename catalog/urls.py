from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),

]
