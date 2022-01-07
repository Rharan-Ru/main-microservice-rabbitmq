from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)


class ProductUser(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
