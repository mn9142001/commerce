from django.db import models

# Create your models here.
class Copoun(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE, null=True, blank=True, related_name='user_copouns')
    category = models.ForeignKey('category.Category', models.SET_NULL, null=True, blank=True, related_name='category_copouns')
    product = models.ForeignKey('category.Product', models.SET_NULL, null=True, blank=True, related_name='product_copouns')
    order = models.ForeignKey('orders.Order', models.SET_NULL, null=True, blank=True, related_name='order_copouns')
    used = models.BooleanField(default=False)
    money = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    expire = models.DateTimeField(null=True)
    binary = models.UUIDField()