from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Profile, Category
from .forms import SignUpForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


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


class CategoryList(ListView):
    template_name = 'category_list.html'
    model = Category
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    template_name = 'category_detail.html'
    model = Category
    context_object_name = 'category'


class CategoryCreate(CreateView):
    template_name = 'category_create.html'
    model = Category
    success_url = reverse_lazy('category_list')
    fields = '__all__'


class CategoryUpdate(UpdateView):
    template_name = 'category_update.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_detail')
    context_object_name = 'category'


class CategoryDelete(DeleteView):
    template_name = 'category_delete.html'
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')
