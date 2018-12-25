from django import forms
from django.forms import ModelForm
from .models import Category
from .models import Product, Category


# class AddProduct(forms.Form):
#     title = forms.CharField(label='Название', max_length=250)
#     snippet = forms.CharField(widget=forms.Textarea, required=False, label='Описание')
#     image = forms.ImageField(label='Картинка')
#     cost = forms.DecimalField(
#         widget=forms.NumberInput(
#             attrs={'value': '0'}
#         ),
#         label='Цена',
#         max_digits=12,
#         decimal_places=2,
#         required=False
#     )
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', required=False)

class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'category', 'image',
            'snippet', 'cost'
        ]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'snippet']