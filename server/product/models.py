from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    snippet = models.TextField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=250)
    snippet = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='products')
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
