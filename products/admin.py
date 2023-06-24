from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin): #managing models in the admin area
    list_display = ('name', 'price', 'stock') #deside how the list going to display


admin.site.register(Product, ProductAdmin)

