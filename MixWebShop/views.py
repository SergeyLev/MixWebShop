from django.shortcuts import render
from .models import ShippingAddress, Person, Product, Admin, Category, User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView


class ShippingAddress(DetailView):
    template_name = 'shipping_address.html'
    model = ShippingAddress
    context_object_name = 'shipping_adress'

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
