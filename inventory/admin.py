from django.contrib import admin
from .models import Product, Category, StockControl,Image, Inventory,AttributeValue,Attribute

# Register your models here.


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Attribute)
# admin.site.register(AttributeValue)
# admin.site.register(Inventory)
# admin.site.register(Image)
# admin.site.register(StockControl)

class ProductImageInline(admin.TabularInline):
    model = Image


class StockControlInline(admin.TabularInline):
    model = StockControl    

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue






@admin.register(Inventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines= [ProductImageInline, StockControlInline]   

@admin.register(Attribute)
class ProductAdmin(admin.ModelAdmin):
    inlines= [AttributeValueInline,]   

  
@admin.register(Category)
class GategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {
            "slug":("name",),
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        prepopulated_fields = {
            "slug":("the_name",),
        }        