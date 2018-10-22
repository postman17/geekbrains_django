from django.shortcuts import render

# Create your views here.
import json

def view_products(request):

    with open('server/data/data.json', encoding='utf-8') as file:
        data = json.load(file)
    context = {
       'products': data['products']
    }
    return render(request, 'product/product.html', context)

def details(request, product_name, product_content):
    context = {
        'name': product_name,
        'content': product_content
    }
    return render(request, 'product/details.html', context)