from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Category, Product, Blog


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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'img', 'activate')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'img', 'activate')
    # success_url = reverse_lazy('catalog:blog_list')

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(activate=True)
        return  queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        blog_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['blog_pk'] = blog_item.pk,
        context_data['title'] = f'{blog_item.title}(slug = {blog_item.slug})'

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object
