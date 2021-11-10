from django.db import models
from django.contrib.auth.models import User


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
    image = models.URLField(null=True, blank=True, help_text='Insert link here')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField()
    wish_list = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_basket_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_basket_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=50, null=False)
    district = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=50, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
