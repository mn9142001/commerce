from django.db import models

def sub_product_file_handler(instance, filename):
    return f"category-{instance.product.sub_category.category.name}/sub-{instance.product.sub_category.name}/{instance.product.id}-{instance.product.name}/{instance.id}-{instance.description}/{filename}"

def product_file_handler(instance, filename):
    return f"category-{instance.sub_category.category.name}/sub-{instance.sub_category.name}/{instance.id}-{instance.name}/{filename}"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, null=True, blank=True, related_name='category_subs')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, models.CASCADE, null=True, blank=True, related_name='sub_products')
    name = models.TextField(max_length=1000)
    description = models.TextField(max_length=10000)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to=product_file_handler, null=True)

    def get_img(self):
        if self.img:
            return f"/media/{self.img}"
        return f"/media/defaults/product.png"

    def get_price(self, copoun=None):
        if self.discount:
            return self.price - self.discount
        return self.price

class SubProduct(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_versions')
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to=sub_product_file_handler,null=True)


