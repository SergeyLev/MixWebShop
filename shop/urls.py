"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MixWebShop.views import (Main, ProductList, ProductDetail, ProductCreate,
                              ProductUpdate, ProductDelete, UserRegisterView, ProfileUpdate, ProfileDetail, ProfileEdit,
                              CategoryList, CategoryDetail, PasswordsChangeView, ProfileCreat,
                              CategoryCreate, CategoryUpdate, CategoryDelete, password_success, basket, checkout,
                              updateItem, search_results)

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    path('products', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/detail', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:pk>/detail/delete', ProductDelete.as_view(), name='product_delete'),
    path('products/<int:pk>/detail/update', ProductUpdate.as_view(), name='product_update'),
    path('products/create', ProductCreate.as_view(), name='product_create'),
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile_update', ProfileUpdate.as_view(), name='profile_update'),
    path('accounts/profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('accounts/profile/<int:pk>/edit_public_profile', ProfileEdit.as_view(), name='edit_public_profile'),
    path('accounts/profile/create', ProfileCreat.as_view(), name='profile_create'),
    path('category', CategoryList.as_view(), name='category_list'),
    path('category/create', CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/detail', CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/detail/update', CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/detail/delete', CategoryDelete.as_view(), name='category_delete'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'),
         name='change_password'),
    path('password_success', password_success, name='password_success'),
    path('basket/', basket, name='basket'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('search_results/', search_results, name='search_results'),

]
