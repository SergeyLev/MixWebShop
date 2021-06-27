from django.db import models


class ShippingAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    country = models.TextField(max_length=100, null=False)
    city = models.TextField(max_length=50, null=False)
    zip_code = models.TextField(max_length=20, null=False)
    phone = models.IntegerField(blank=True)


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False)
    surname = models.TextField(max_length=100, null=False)
    date_of_birth = models.DateField(max_length=10)


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(to=Person, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
