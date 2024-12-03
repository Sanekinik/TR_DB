from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['fullname', 'dateofbirth', 'phone']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['fullname', 'phone', 'roleid', 'workstartdate', 'salary']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['productname', 'categoryid', 'supplierid', 'quantityinstock', 'price']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['rolename']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ['suppliername']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['productid', 'clientid', 'quantity', 'transactiondate', 'employeeid']