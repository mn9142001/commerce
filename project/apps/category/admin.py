from django.contrib import admin
from .models import Category, SubCategory, Product, SubProduct
# Register your models here.
admin.site.register([Category, SubCategory, Product, SubProduct])