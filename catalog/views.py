from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/home.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все товары  категории: {category_item.name}'
    }
    return render(request, 'catalog/products.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': Product.objects.get(pk=pk)
        'description': f'{product_item.description}',
        'title': f'{product_item.name}'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты '
    }
    return render(request, 'catalog/contacts.html', context)
