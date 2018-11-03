from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Category, Product
from images.models import Image
from .forms import AddProduct
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.


def view_products(request):
    query = get_list_or_404(Product)
    page = request.GET.get('page')
    paginator = Paginator(query, 3)
    products = paginator.get_page(page)

    return render(request, 'product/product.html', {'products': products})


def details(request, product_name, product_content, product_image):
    context = {
        'name': product_name,
        'content': product_content,
        'image': product_image
    }
    return render(request, 'product/details.html', context)


def add_product(request):
    success_url = reverse_lazy('product:index')
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST) #,request.FILES
        if form.is_valid():
            # try:
            #     load_category = Category.objects.get(title=form.cleaned_data['category'])
            # except Exception:
            #     load_category = None
            # load_image = Image.objects.create(
            #     title=form.cleaned_data['title'],
            #     value=form.cleaned_data['image']
            # )
            # add = Product.objects.create(
            #     title=form.cleaned_data['title'],
            #     snippet=form.cleaned_data['snippet'],
            #     cost=form.cleaned_data['cost'],
            #     category=load_category,
            #     image=load_image
            # )
            form.save()
            return redirect(success_url)

    return render(request, 'product/add.html', {'form': form})

def update_product(request, pk):
    success_url = reverse_lazy('product:index')
    obj = get_object_or_404(Product, pk=pk)
    form = AddProduct(instance=obj)
    if request.method == 'POST':
        form = AddProduct(
            request.POST,
            files=request.FILES,
            instance=obj
            )
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, 'product/update.html', {'form': form, 'obj': obj})

def delete_product(request, pk):
    success_url = reverse_lazy('product:index')
    obj = get_object_or_404(Product, pk=pk)
    form = AddProduct(instance=obj)
    if request.method == 'POST':
        obj.delete()
        return redirect(success_url)
    return render(request, 'product/delete.html', {'obj': obj})