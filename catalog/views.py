from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


# def home(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории товаров'
#     }
#     return render(request, 'catalog/category_list.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }


# def products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Все товары  категории: {category_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Все товары категории: {category_item.name}'

        return context_data


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'description': product_item.description,
#         'title': f'{product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product

    # extra_context = {
    #     'title': model.name,
    # }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk,
        context_data['title'] = f'{product_item.name}'

        return context_data


def contacts(request):
    context = {
        'title': 'Контакты '
    }
    return render(request, 'catalog/contacts.html', context)
