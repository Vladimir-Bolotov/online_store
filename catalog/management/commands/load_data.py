from catalog.models import Category
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', 'category_data.json')
        call_command('loaddata', 'product_data.json')
