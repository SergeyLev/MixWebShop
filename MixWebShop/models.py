from django.db import models

class Person(models.Model):
    name = models.TextField(max_length=100, null=False)
    surname = models.TextField(max_length=100, null=False)
    date_of_birth = models.DateField(max_length=10)

class ShippingAddress(models.Model):
    name = models.ForeignKey(Person, null=False, on_delete=models.DO_NOTHING)
    surname = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    country = models.TextField(max_length=100, null=False)
    city = models.TextField(max_length=50, null=False)
    zip_code = models.TextField(max_length=20, null=False)
    phone = models.IntegerField(blank=True)
