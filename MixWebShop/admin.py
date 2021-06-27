from django.contrib import admin
from .models import ShippingAddress, Person, Product, Admin, Category, User

admin.site.register(ShippingAddress)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(User)
