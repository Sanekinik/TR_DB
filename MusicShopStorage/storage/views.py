from django.shortcuts import render
from .models import *
from MusicShopStorage.settings import get_db_connection # подключение к БД
from django.http import HttpResponse, HttpResponseRedirect

# Панель выбора роли
def home(request):
    return render(request, 'storage/index.html')

# Панель работника
def index(request, role):
    return render(request, f'{role}/index.html')

# Отображение таблицы клиентов
def clients_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients ORDER BY clientid;')
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'clients': clients,
    }
    return render(request, f'{role}/clients.html', context)

# Представление для добавления клиентов
def client_add(request, role):
    fullname = request.POST.get("fullname", "Undefined")
    dateofbirth = request.POST.get("dateofbirth", "Undefined")
    phone = request.POST.get("phone", "Undefined")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT check_client(%s);", (phone,))
    if not cursor.fetchone()[0]:
        cursor.execute("SELECT add_client(%s, %s, %s);", (fullname, dateofbirth, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/clients/" + role)
    
    else:
        cursor.close()
        conn.close()
        return HttpResponse('Пользователь с таким номером телефона уже есть в базе данных')
    
# Представление для редактирования клиентов
def client_edit(request, role):
    clientid = request.POST.get("id")
    fullname = request.POST.get("fullname", "Undefined")
    dateofbirth = request.POST.get("dateofbirth", "Undefined")
    phone = request.POST.get("phone", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT update_client(%s, %s, %s, %s);", (clientid, fullname, dateofbirth, phone))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponseRedirect("/clients/" + role)
    
# Представление для удаления клиентов
def client_delete(request, role):
    clientid = request.POST.get("id", "0")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT delete_client(%s);", (clientid,))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponseRedirect("/clients/" + role)

# Отображение таблицы работников
def employees_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM get_employees_with_roles() ORDER BY employeeid;')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'employees': employees,
    }
    return render(request, f'{role}/employees.html', context)

# Представление для добавления работников
def employee_add(request, role):
    fullname = request.POST.get("fullname", "Undefined")
    phone = request.POST.get("phone", "Undefined")
    rolename = request.POST.get("role", "Undefined")
    workstartdate = request.POST.get("workstartdate", "Undefined")
    salary = request.POST.get("salary", "Undefined")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT check_client(%s);", (phone,))
    if not cursor.fetchone()[0]:
        cursor.execute("SELECT add_employee_with_role(%s, %s, %s, %s, %s);", (fullname, phone, rolename, workstartdate, salary))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/employees/" + role)
    else:
        cursor.close()
        conn.close()
        return HttpResponse('Работник с таким номером телефона уже есть в базе данных')
    
# Представление для редактирования работников
def employee_edit(request, role):
    employeeid = request.POST.get("id")
    fullname = request.POST.get("fullname", "Undefined")
    phone = request.POST.get("phone", "Undefined")
    rolename = request.POST.get("role", "Undefined")
    workstartdate = request.POST.get("workstartdate", "Undefined")
    salary = request.POST.get("salary", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT update_employee(%s, %s, %s, %s, %s, %s);", (employeeid, fullname, phone, rolename, workstartdate, salary))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/employees/" + role)
    except:
        cursor.close()
        conn.close()
        return HttpResponse("Некорректные данные")
    
# Представление для удаления работников
def employee_delete(request, role):
    employeeid = request.POST.get("id", "0")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT delete_employee(%s);", (employeeid,))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponseRedirect("/employees/" + role)

# Отображение таблицы категорий продуктов
def productcategories_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Получение данных из таблицы Productcategories
    cursor.execute('SELECT * FROM productcategories ORDER BY categoryid;')
    productcategories = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'productcategories': productcategories,
    }
    return render(request, f'{role}/productcategories.html', context)

# Представление для добавления категорий продуктов
def productcategory_add(request, role):
    categoryname = request.POST.get("categoryname", "Undefined")
    category = Productcategories(categoryname=categoryname)
    category.save()
    return HttpResponseRedirect("/productcategories/" + role)
    
# Представление для редактирования категорий продуктов
def productcategory_edit(request, role):
    categoryid = request.POST.get("id")
    categoryname = request.POST.get("categoryname", "Undefined")
    Productcategories.objects.filter(categoryid=categoryid).update(categoryname=categoryname)
    return HttpResponseRedirect("/productcategories/" + role)
    
# Представление для удаления категорий продуктов
def productcategory_delete(request, role):
    categoryid = request.POST.get("id")
    try:
        Productcategories.objects.filter(categoryid=categoryid).delete()
        return HttpResponseRedirect("/productcategories/" + role)
    except:
        return HttpResponse("Ещё существуют продукты из данной категории")

# Отображение таблицы продуктов
def products_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product_details ORDER BY productid;')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'products': products,
    }
    return render(request, f'{role}/products.html', context)

# Представление для добавления продуктов
def product_add(request, role):
    productname = request.POST.get("productname", "Undefined")
    categoryname = request.POST.get("categoryname", "Undefined")
    suppliername = request.POST.get("suppliername", "Undefined")
    quantityinstock = request.POST.get("quantityinstock", "Undefined")
    price = request.POST.get("price", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT add_product(%s, %s, %s, %s, %s);", (productname, categoryname, suppliername,quantityinstock, price))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/products/" + role)
    except:
        cursor.close()
        conn.close()
        return HttpResponse('Некорректные данные продукта')
    
# Представление для редактирования продуктов
def product_edit(request, role):
    productid = request.POST.get("id", "Undefined")
    productname = request.POST.get("productname", "Undefined")
    categoryname = request.POST.get("categoryname", "Undefined")
    suppliername = request.POST.get("suppliername", "Undefined")
    quantityinstock = request.POST.get("quantityinstock", "Undefined")
    price = request.POST.get("price", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT update_product(%s, %s, %s, %s, %s, %s);", (productid, productname, categoryname, suppliername,quantityinstock, price))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/products/" + role)
    except:
        cursor.close()
        conn.close()
        return HttpResponse('Некорректные данные продукта')
    
# Представление для удаления продуктов
def product_delete(request, role):
    productid = request.POST.get("id")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT delete_product(%s);", (productid,))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponseRedirect("/products/" + role)

# Отображение таблицы поставщиков
def suppliers_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM suppliers ORDER BY supplierid;')
    suppliers = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'suppliers': suppliers,
    }
    return render(request, f'{role}/suppliers.html', context)

# Представление для добавления поставщиков
def supplier_add(request, role):
    suppliername = request.POST.get("suppliername", "Undefined")
    supplier = Suppliers(suppliername=suppliername)
    supplier.save()
    return HttpResponseRedirect("/suppliers/" + role)
    
# Представление для редактирования поставщиков
def supplier_edit(request, role):
    supplierid = request.POST.get("id")
    suppliername = request.POST.get("suppliername", "Undefined")
    Suppliers.objects.filter(supplierid=supplierid).update(suppliername=suppliername)
    return HttpResponseRedirect("/suppliers/" + role)
    
# Представление для удаления поставщиков
def supplier_delete(request, role):
    supplierid = request.POST.get("id")
    try:
        Suppliers.objects.filter(supplierid=supplierid).delete()
        return HttpResponseRedirect("/suppliers/" + role)
    except:
        return HttpResponse("Ещё существуют продукты от данного поставщика")

# Отображение таблицы транзакций
def transactions_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transaction_details ORDER BY transactionid;')
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'transactions': transactions,
    }
    return render(request, f'{role}/transactions.html', context)

# Представление для добавления транзакций
def transaction_add(request, role):
    productname = request.POST.get("productname", "Undefined")
    clientphone = request.POST.get("clientphone", "Undefined")
    quantity = request.POST.get("quantity", "Undefined")
    transactiondate = request.POST.get("transactiondate", "Undefined")
    employeeid = request.POST.get("employeeid", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT add_transaction(%s, %s, %s, %s, %s);", (productname, clientphone, quantity, transactiondate, employeeid))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/transactions/" + role)
    except:
        cursor.close()
        conn.close()
        return HttpResponse('Неверные данные транзакции')
    
# Представление для редактирования транзакций
def transaction_edit(request, role):
    transactionid = request.POST.get("id")
    productname = request.POST.get("productname", "Undefined")
    clientphone = request.POST.get("clientphone", "Undefined")
    quantity = request.POST.get("quantity", "Undefined")
    transactiondate = request.POST.get("transactiondate", "Undefined")
    employeeid = request.POST.get("employeeid", "Undefined")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT update_transaction(%s, %s, %s, %s, %s, %s);", (transactionid, productname, clientphone, quantity, transactiondate, employeeid))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect("/transactions/" + role)
    except:
        cursor.close()
        conn.close()
        return HttpResponse('Неверные данные транзакции')
    
# Представление для удаления транзакций
def transaction_delete(request, role):
    transactionid = request.POST.get("id")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT delete_transaction(%s);", (transactionid))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponseRedirect("/transactions/" + role)

# Отображение таблицы ролей
def roles_list(request, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM roles ORDER BY roleid;')
    roles = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'roles': roles,
    }
    return render(request, f'{role}/roles.html', context)

# Представление для добавления ролей
def role_add(request, role):
    rolename = request.POST.get("rolename", "Undefined")
    role_ = Roles(rolename=rolename)
    role_.save()
    return HttpResponseRedirect("/roles/" + role)
    
# Представление для редактирования ролей
def role_edit(request, role):
    roleid = request.POST.get("id")
    rolename = request.POST.get("rolename", "Undefined")
    Roles.objects.filter(roleid=roleid).update(rolename=rolename)
    return HttpResponseRedirect("/roles/" + role)
    
# Представление для удаления ролей
def role_delete(request, role):
    roleid = request.POST.get("id")
    Roles.objects.filter(roleid=roleid).delete()
    return HttpResponseRedirect("/roles/" + role)