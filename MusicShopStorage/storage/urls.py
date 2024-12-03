from django.urls import path
from .views import *

urlpatterns = [
    # Главная страница
    path('', home, name='home'),

    # Страница с таблицами
    path('index/<str:role>/', index, name='index'),
    
    # Таблицы
    path('employees/<str:role>/', employees_list, name='employees'),
    path('productcategories/<str:role>/', productcategories_list, name='productcategories'),
    path('products/<str:role>/', products_list, name='products'),
    path('suppliers/<str:role>/', suppliers_list, name='suppliers'),
    path('transactions/<str:role>/', transactions_list, name='transactions'),
    path('roles/<str:role>/', roles_list, name='roles'),
]