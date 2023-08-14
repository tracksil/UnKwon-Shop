from django.db import models

from apps.products.models import Product
from apps.users.models import User


class WishList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "wish_list"


class WishListProducts(models.Model):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "wish_list_products"
