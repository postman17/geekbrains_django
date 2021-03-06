from django.core.management.base import BaseCommand, CommandError
from product.models import Product
from images.models import Image
import json


class Command(BaseCommand):
    help = 'Add data form file into database.'

    def handle(self, *args, **options):
        with open('server/data/data.json', encoding='utf-8') as file:
            data = json.load(file)
        try:
            for value in data['products']:
                Product.objects.get(title=value['name'])
            self.stdout.write(self.style.SUCCESS('All records already exists'))
        except Exception:
            image = Image.objects.get(title='default')
            for item in data['products']:
                main = Product()
                main.title = item['name']
                main.snippet = item['content']
                main.image = image
                main.save()
            self.stdout.write(self.style.SUCCESS('Operation success!'))