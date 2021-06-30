from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return self.user.username


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Primary key
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign Key
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name