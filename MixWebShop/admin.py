from django.contrib import admin
from .models import Product, Category, Profile, Order, OrderItem, ShippingAddress

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
