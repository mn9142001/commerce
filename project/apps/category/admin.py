from django.contrib import admin
from .models import Category, SubCategory, Product, SubProduct
# Register your models here.
admin.site.register([Category, SubCategory, Product, SubProduct])


# _list = {'electronics' : ['graphics', 'cpus', 'ram', 'power supply', 'cases', 'storage'], 'clothers': ['shirts', 'shoes', 'pants', 'dress']}
# for key, value in _list.items():
#     cat = Category.objects.create(name=key)
#     for sub in value:
#         SubCategory.objects.create(name=sub, category=Category.objects.last())