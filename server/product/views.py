from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
import json

def view_products(request):
    with open('server/data/data.json', encoding='utf-8') as file:
        data = json.load(file)
    try:
        Product.objects.get(title=data['products'][0]['name'])
    except Exception:
        for item in data['products']:
            main = Product()
            main.title = item['name']
            main.snippet = item['content']
            main.save()
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product/product.html', context)



def details(request, product_name, product_content):
    context = {
        'name': product_name,
        'content': product_content
    }
    return render(request, 'product/details.html', context)