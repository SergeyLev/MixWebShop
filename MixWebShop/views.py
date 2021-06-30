from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Product, Profile
from .forms import SignUpForm
from django.urls import reverse_lazy


class Main(TemplateView):
    template_name = 'main.html'


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductCreate(CreateView):  # with permission
    template_name = 'product_create.html'
    model = Product
    success_url = reverse_lazy('product_list')
    fields = '__all__'


class ProductUpdate(UpdateView):
    template_name = 'product_update.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class ProductDelete(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class SignUpView(CreateView):
    template_name = 'profile_create.html'
    success_url = reverse_lazy('main')
    form_class = SignUpForm


class ProfileDetail(DetailView):
    template_name = 'profile_detail.html'
    model = Profile
    context_object_name = 'profile'


class ProfileUpdate(UpdateView):
    template_name = 'profile_update.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('profile_detail')
    context_object_name = 'profile'
