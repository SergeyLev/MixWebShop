from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import Product, Category, Profile, Order, OrderItem
from .forms import SignUpForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse


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


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class ProfileUpdate(UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('main')

    def get_object(self, **kwargs):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ProfileDetail(DetailView):
    template_name = 'registration/profile_detail.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class ProfileEdit(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['name', 'last_name', 'email']
    success_url = reverse_lazy('main')


class ProfileCreat(CreateView):
    model = Profile
    fields = ['name', 'last_name', 'email']
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


def basket(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer,
                                                     delivered=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        try:
            basket = json.loads(request.COOKIES['basket'])
        except:
            basket = {}
            print('BASKET:', basket)
        items = []
        order = {'get_basket_total': 0, 'get_basket_items': 0}
        basketItems = order['get_basket_items']
    context = {'items': items, 'order': order, 'basketItems': basketItems}
    return render(request, 'basket/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, delivered=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total': 0, 'get_car_items': 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'basket/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.profile
    product = Product.objects.get(product_id=productId)
    order, created = Order.objects.get_or_create(customer=customer, delivered=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def search_results(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains=searched)
        categories = Category.objects.filter(name__contains=searched)
        return render(request,
                      'search_results.html',
                      {'searched': searched,
                       'product': products,
                       'category': categories})
    else:
        return render(request,
                      'search_results.html',
                      {})
