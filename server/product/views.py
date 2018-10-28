from django.shortcuts import render
from product.models import Category, Product

# Create your views here.

def view_products(request):
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