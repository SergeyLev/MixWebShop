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
                              ProductUpdate, ProductDelete, SignUpView,
                              ProfileDetail, ProfileUpdate, CategoryList, CategoryDetail,
                              CategoryCreate, CategoryUpdate, CategoryDelete)

from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    path('products', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/detail', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:pk>/detail/delete', ProductDelete.as_view(), name='product_delete'),
    path('products/<int:pk>/detail/update', ProductUpdate.as_view(), name='product_update'),
    path('products/create', ProductCreate.as_view(), name='product_create'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('accounts/profile/<int:pk>', ProfileDetail.as_view(),  name='profile_detail'),
    path('accounts/profile/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
    path('category', CategoryList.as_view(), name='category_list'),
    path('category/create', CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/detail', CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/detail/update', CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/detail/delete', CategoryDelete.as_view(), name='category_delete'),

]
