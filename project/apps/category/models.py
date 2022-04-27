from django.db import models

def product_file_handler(instance, filename):
    return f"category/{instance.product.sub_category.category.name}/sub/{instance.product.sub_category.name}/{instance.product.id}-{instance.product.name}/{instance.id}-{instance.description}/{filename}"
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, null=True, blank=True, related_name='category_subs')
    name = models.CharField(max_length=255)

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, models.CASCADE, null=True, blank=True, related_name='sub_products')
    name = models.TextField(max_length=1000)
    description = models.TextField(max_length=10000)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=5)
    discount = models.DecimalField(null=True, max_digits=6, decimal_places=5)


    def get_price(self, copoun=None):
        pass

class SubProduct(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_versions')
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to=product_file_handler,null=True)


