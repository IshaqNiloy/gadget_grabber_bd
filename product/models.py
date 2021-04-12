from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=14)
    city = models.CharField(max_length=250)
    post_code = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('product:account')


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    features = models.CharField(max_length=250)
    image = models.FileField()


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    user_name = models.CharField(max_length=250)
    user_address = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    unit_price = models.CharField(max_length=250)
    total_price = models.CharField(max_length=250)