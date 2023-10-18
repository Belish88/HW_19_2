from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Смартфон'},
            {'name': 'Телевизо'},
            {'name': 'Холодильник'},
            {'name': 'Электрочайник'},
            {'name': 'Утюг'},
            {'name': 'Микроволновая печь'},
            {'name': 'Ноутбук'},
        ]
        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
