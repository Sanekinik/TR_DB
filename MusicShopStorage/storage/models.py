# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    clientid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    dateofbirth = models.DateField()
    phone = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'clients'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self):
        return self.fullname


class Employees(models.Model):
    employeeid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    roleid = models.ForeignKey('Roles', models.RESTRICT, db_column='roleid', blank=True, null=True)
    workstartdate = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name_plural = 'Работники'

    def __str__(self) -> str:
        return self.employeeid, self.fullname, self.phone

class Productcategories(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'productcategories'
        verbose_name_plural = 'Категории продуктов'


class Products(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=255)
    categoryid = models.ForeignKey(Productcategories, models.RESTRICT, db_column='categoryid', blank=True, null=True)
    supplierid = models.ForeignKey('Suppliers', models.RESTRICT, db_column='supplierid', blank=True, null=True)
    quantityinstock = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
        verbose_name_plural = 'Продукты'


class Roles(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'roles'
        verbose_name_plural = 'Роли'


class Suppliers(models.Model):
    supplierid = models.AutoField(primary_key=True)
    suppliername = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'suppliers'
        verbose_name_plural = 'Поставщики'


class Transactions(models.Model):
    transactionid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Products, models.CASCADE, db_column='productid', blank=True, null=True)
    clientid = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    transactiondate = models.DateField(blank=True, null=True)
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'
        verbose_name_plural = 'Транзакции'
