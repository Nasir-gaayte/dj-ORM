from email.policy import default
from operator import mod
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.




class Brand(models.Model):
    barna_id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=255)  


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    the_name = models.CharField(max_length=225)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    # qty = models.IntegerField()

    class Meta:
        get_latest_by = ["age"]

    def __str__(self):
        return f"Product name: {self.the_name}"    

class Stock(models.Model):
    units = models.ForeignKey(Brand, on_delete= models.CASCADE)
    product = models.OneToOneField(Product, on_delete= models.CASCADE)