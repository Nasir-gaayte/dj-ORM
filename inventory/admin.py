from django.contrib import admin
from .models import Product, Category, StockControl,Image, Inventory,AttributeValue,Attribute

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Inventory)
admin.site.register(Image)
admin.site.register(StockControl)