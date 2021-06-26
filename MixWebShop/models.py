from django.db import models

class Person(models.Model):
    name = models.TextField(max_length=100, null=False)
    surname = models.TextField(max_length=100, null=False)
    date_of_birth = models.DateField(max_length=10)
    # Admin vai User?

class ShippingAddress(models.Model):
    name = models.ForeignKey(Person, null=False, on_delete=models.DO_NOTHING) # Kads seit datu tips?
    surname = models.ForeignKey(Person, null=False, on_delete=models.CASCADE) # Kads seit datu tips?
    # https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
    
    country = models.TextField(max_length=100, null=False)
    city = models.TextField(max_length=50, null=False)
    zip_code = models.TextField(max_length=20, null=False)
    phone = models.IntegerField(blank=True)

class Category(models.Model):
    name = models.CharField(max_length=150, null=False)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
