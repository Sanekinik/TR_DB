"""
URL configuration for MusicShopStorage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from storage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storage.urls')),
    
    path('clients/<str:role>/', clients_list, name='clients'),
    path('clients/<str:role>/add/', client_add, name='client_add'),
    path('clients/<str:role>/edit/', client_edit, name='client_edit'),
    path('clients/<str:role>/delete/', client_delete, name='client_delete'),

    path('employees/<str:role>/', employees_list, name='employees'),
    path('employees/<str:role>/add/', employee_add, name='employee_add'),
    path('employees/<str:role>/edit/', employee_edit, name='employee_edit'),
    path('employees/<str:role>/delete/', employee_delete, name='employee_delete'),

    path('productcategories/<str:role>/', productcategories_list, name='productcategories'),
    path('productcategories/<str:role>/add/', productcategory_add, name='productcategory_add'),
    path('productcategories/<str:role>/edit/', productcategory_edit, name='productcategory_edit'),
    path('productcategories/<str:role>/delete/', productcategory_delete, name='productcategory_delete'),

    path('products/<str:role>/', products_list, name='products'),
    path('products/<str:role>/add/', product_add, name='product_add'),
    path('products/<str:role>/edit/', product_edit, name='product_edit'),
    path('products/<str:role>/delete/', product_delete, name='product_delete'),

    path('roles/<str:role>/', roles_list, name='roles'),
    path('roles/<str:role>/add/', role_add, name='role_add'),
    path('roles/<str:role>/edit/', role_edit, name='role_edit'),
    path('roles/<str:role>/delete/', role_delete, name='role_delete'),

    path('suppliers/<str:role>/', suppliers_list, name='suppliers'),
    path('suppliers/<str:role>/add/', supplier_add, name='supplier_add'),
    path('suppliers/<str:role>/edit/', supplier_edit, name='supplier_edit'),
    path('suppliers/<str:role>/delete/', supplier_delete, name='supplier_delete'),

    path('transactions/<str:role>/', transactions_list, name='transactions'),
    path('transactions/<str:role>/add/', transaction_add, name='transaction_add'),
    path('transactions/<str:role>/edit/', transaction_edit, name='transaction_edit'),
    path('transactions/<str:role>/delete/', transaction_delete, name='transaction_delete'),
]