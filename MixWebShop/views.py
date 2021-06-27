from django.shortcuts import render
from .models import ShippingAddress, Person, Product, Admin, Category, User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView

class Main(TemplateView):
    template_name = 'main.html'


class DetailShippingAddress(DetailView):
    template_name = 'shipping_address.html'
    model = ShippingAddress
    context_object_name = 'shipping_address'


class CreateShippingAddress(CreateView):
    template_name = 'create_shipping_address.html'
    model = ShippingAddress
    success_url = reverse_lazy('shipping_address')
    fields = '__all__'


class UpdateShippingAddress(UpdateView):
    template_name = 'update_shipping_address.html'
    model = ShippingAddress
    success_url = reverse_lazy('shipping_address')
    fields = '__all__'
    context_object_name = 'address'


class DeleteShippingAddress(DeleteView):
    template_name = 'delete_shipping_address.html'
    model = ShippingAddress
    context_object_name = 'address'
    success_url = reverse_lazy('shipping_address')


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'


class DetailProduct(DetailView):
    template_name = 'detail_product.html'
    model = Product
    context_object_name = 'product'


class CreateProduct(CreateView):  # with permision
    template_name = 'create_product.html'
    model = Product
    success_url = reverse_lazy('products')
    fields = '__all__'


class ProductUpdate(UpdateView):
    template_name = 'create_product.html'
    model = Product
    success_url = reverse_lazy('products')
    context_object_name = 'product'


class ProductDelete(DeleteView):
    template_name = 'delete_product.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')


class CategoryList(ListView):
    template_name = 'category_list.html'
    model = Category
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    template_name = 'category_detail.html'
    model = Category
    context_object_name = 'category'


class CategoryCreate(CreateView):  # with permission
    template_name = 'category_create.html'
    model = Category
    success_url = reverse_lazy('categories')
    fields = '__all__'


class CategoryUpdate(UpdateView):   # with permission
    template_name = 'create_product.html'
    model = Category
    success_url = reverse_lazy('categories')
    context_object_name = 'category'


class CategoryDelete(DeleteView):   # with permission
    template_name = 'delete_category.html'
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('categories')


class PersonDetail(DetailView):
    template_name = 'person_detail.html'
    model = Person
    context_object_name = 'person'

class PersonCreate(CreateView):
    template_name = 'person_create.html'
    model = Person
    success_url = reverse_lazy('person')
    fields = '__all__'


class PersonUpdate(UpdateView):
    template_name = 'person_create.html'
    model = Person
    success_url = reverse_lazy('person')
    context_object_name = 'person'


class PersonDelete(DeleteView):
    template_name = 'person_delete.html'
    model = Person
    context_object_name = 'person'
    success_url = reverse_lazy('person')