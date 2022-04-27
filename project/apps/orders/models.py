from django.db import models

# Create your models here.


class Order(models.Model):
    choices = ((1, 'waiting'), (2,'shipped'), (3, 'arrived'))
    products = models.ManyToManyField('category.Product', related_name='product_orders')
    price = models.DecimalField(max_digits=6, decimal_places=5)
    discount = models.DecimalField(max_digits=6,null=True, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=choices)
    arrival = models.DateField(null=True, blank=True)
    def get_price(self, copoun=None):
        pass
