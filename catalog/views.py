from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    context = {
        'object_list': Product.objects.filter(),
        'title': 'Все товары категории '
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
