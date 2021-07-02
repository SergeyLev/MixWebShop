from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.TextField(max_length=100, null=True)
    surname = models.TextField(max_length=100, null=True)
    date_of_birth = models.DateField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Primary key
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Foreign Key
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


