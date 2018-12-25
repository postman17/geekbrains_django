# from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Category, Product
#from .forms import AddProduct
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.mixins import AdminRoleRequired


class ProductJsonListView(ListView):
    model = Product
    paginate_by = 10

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'title': itm.title,
                    'category': str(itm.category) if itm.category else None,
                    'image': itm.image.url,
                    'cost': itm.cost,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(ProductJsonListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:list')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number()}'

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class ProductCreate(LoginRequiredMixin, AdminRoleRequired, CreateView):
    model = Product
    fields = [
        'title', 'category', 'image',
        'snippet', 'cost'
    ]
    template_name = 'product/add.html'
    success_url = reverse_lazy('product:index')
    login_url = reverse_lazy('accounts:login')


class ProductUpdate(LoginRequiredMixin, AdminRoleRequired, UpdateView):
    model = Product
    fields = [
        'title', 'category', 'image',
        'snippet', 'cost'
    ]
    template_name = 'product/add.html'
    success_url = reverse_lazy('product:index')
    login_url = reverse_lazy('accounts:login')


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product/add.html'
    success_url = reverse_lazy('product:index')
    login_url = reverse_lazy('accounts:login')

    def test_func(self):
        return self.request.user.is_superuser

class ProductList(ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'products'
    paginate_by = 3


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/details.html'


class CategoryList(ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'
    paginate_by = 10


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        page = self.request.GET.get('page')
        paginator = Paginator(obj.product_set.all(), 10)
        page_obj = paginator.get_page(page)
        return {
            'object': obj,
            'objects_list': page_obj.object_list,
            'paginator': paginator,
            'page_obj': page_obj
        }

# def view_products(request):
#     query = get_list_or_404(Product)
#     page = request.GET.get('page')
#     paginator = Paginator(query, 3)
#     products = paginator.get_page(page)
#
#     return render(request, 'product/product.html', {'products': products})


# def details(request, pk):
#     obj = get_object_or_404(Product, pk=pk)
#     context = {
#         'name': obj.title,
#         'content': obj.snippet,
#         'image': obj.image
#     }
#     return render(request, 'product/details.html', context)

#
# def add_product(request):
#     success_url = reverse_lazy('product:index')
#     form = AddProduct()
#     if request.method == 'POST':
#         form = AddProduct(request.POST) #,request.FILES
#         if form.is_valid():
#             # try:
#             #     load_category = Category.objects.get(title=form.cleaned_data['category'])
#             # except Exception:
#             #     load_category = None
#             # load_image = Image.objects.create(
#             #     title=form.cleaned_data['title'],
#             #     value=form.cleaned_data['image']
#             # )
#             # add = Product.objects.create(
#             #     title=form.cleaned_data['title'],
#             #     snippet=form.cleaned_data['snippet'],
#             #     cost=form.cleaned_data['cost'],
#             #     category=load_category,
#             #     image=load_image
#             # )
#             form.save()
#             return redirect(success_url)
#
#     return render(request, 'product/add.html', {'form': form})

# def update_product(request, pk):
#     success_url = reverse_lazy('product:index')
#     obj = get_object_or_404(Product, pk=pk)
#     form = AddProduct(instance=obj)
#     if request.method == 'POST':
#         form = AddProduct(
#             request.POST,
#             files=request.FILES,
#             instance=obj
#             )
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     return render(request, 'product/update.html', {'form': form, 'obj': obj})

# def delete_product(request, pk):
#     success_url = reverse_lazy('product:index')
#     obj = get_object_or_404(Product, pk=pk)
#     form = AddProduct(instance=obj)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect(success_url)
#     return render(request, 'product/delete.html', {'obj': obj})


# def category_list(request):
#     query = get_list_or_404(Category)
#     page = request.GET.get('page')
#     paginator = Paginator(query, 3)
#     categories = paginator.get_page(page)
#     return render(request, 'categories/list.html', {'categories': categories})


# def category_detail(request, pk):
#     obj = get_object_or_404(Category, pk=pk)
#     page = request.GET.get('page')
#     paginator = Paginator(obj.product_set.all(), 3)
#     results = paginator.get_page(page)
#     return render(request, 'categories/detail.html', {
#         'object': obj,
#         'results': results})