from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Products)
admin.site.register(Clients)
admin.site.register(Employees)
admin.site.register(Productcategories)
admin.site.register(Roles)
admin.site.register(Suppliers)
admin.site.register(Transactions)