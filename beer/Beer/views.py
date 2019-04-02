# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from Beer.models import *
from django.http import JsonResponse,HttpResponse
import hashlib
import os
import base64
import datetime
import json
from collections import Iterable
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.http import HttpResponseRedirect
@csrf_exempt
def hash_code(s):  # 加点盐
    h = hashlib.sha256()
    salt = 'mysite'
    c = salt+s
    h.update(c.encode())  # update方法只接收bytes类型
    return h.hexdigest()
def Dashboard(request):
    return render_to_response("dashborad.html")
def Tem_addMaintenance(request):
    return render_to_response("Tem_addMaintenance.html")
def Maintenance(request):
    return render_to_response("Maintenance.html")
def home(request):
    return render_to_response("index.html")
def Supplier(request):
    return render_to_response("Supplier.html")
def Purchase(request):
    return render_to_response("Purchase.html")
def Tem_addPurchase(request):
    return render_to_response("Tem_addPurchase.html")
def Material(request):
    return render_to_response("Material.html")
def Product(request):
    return render_to_response("Product.html")
def Orders1(request):
    return render_to_response("Orders.html")
def Customers1(request):
    return render_to_response("Customers.html")
def Equipment(request):
    return render_to_response("Equipment.html")
def Warehouse1(request):
    return render_to_response("Warehouse.html")
def Labor(request):
    return render_to_response("Labor.html")
def Activity(request):
    return render_to_response("Activity.html")
def Tem_addOrder(request):
    return render_to_response("Tem_addOrder.html")
def Tem_addActivity(request):
    return render_to_response("Tem_addActivity.html")
def login(request):
    if request.method =="POST":
        success = None
        try:
            username = request.POST['username']
            password = request.POST['password']
            if username and password:  # 确保用户名和密码都不为空

                username = username.strip()
                # 用户名字符合法性验证
                # 密码长度验证
                # 更多的其它验证.....
                try:
                    user = administrators.objects.get(Admin_Username=username)
                    if user.Admin_Password == password:
                        message = "登陆成功！"
                        success = True
                    else:
                        success = False
                        Data = "密码不正确！"
                except:
                    success = False
                    Data = "用户名不存在！"
        except Exception as e:
            success = False
            Data = str(e)
        # return JsonResponse({"success": success, "data": Data})
        if success == True:

            # return render_to_response("index.html")
            return render(request,'dashborad.html')
        else:
            # return HttpResponseRedirect("SupplierMgt")
            return HttpResponse("Login Failed. Please check your username and password.")

def register(request):
    if request.method == "POST":
        Data = []
        try:
            username = json.loads(request.body)['username']
            password = json.loads(request.body)['password']
            WorkNum = json.loads(request.body)['worknum']
            same_name_user = administrators.objects.filter(Admin_Username=username)
            if same_name_user:  # 用户名唯一
                Data = '用户已经存在，请重新选择用户名！'
                success = False
                return JsonResponse({"success": success, "data": Data})
            worknum_check = administrators.objects.filter(WorkNum_id = WorkNum)
            if worknum_check:  # 用户名唯一
                administrators.objects.create(Admin_Username=username, Admin_Password=hash_code(password), WorkNum_id = WorkNum)
                message = "注册成功"
                success = True
                return JsonResponse({"success": success, "data": Data})
            else:
                Data = '工号错误'
                success = False
                return JsonResponse({"success": success, "data": Data})
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Supplier_Mgt(request):
    if request.method == "GET":
        SuppliersInfo = suppliers.objects.all()
        Data = []
        try:
            success = True
            if SuppliersInfo:
                if isinstance(SuppliersInfo, Iterable) == True:
                    for Supplier in SuppliersInfo:
                        Supplier_Id = Supplier.Supplier_Id
                        Supplier_Name = Supplier.Supplier_Name
                        Material_id = Supplier.Material_id
                        Liaison_Name = Supplier.Liaison_Name
                        Liaison_Number = Supplier.Liaison_Number
                        Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
                                    "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
                        Data.append(Supplierinfo)
                else:
                    Supplier_Id = SuppliersInfo.Supplier_Id
                    Supplier_Name = SuppliersInfo.Supplier_Name
                    Material_id = SuppliersInfo.Material_id
                    Liaison_Name = SuppliersInfo.Liaison_Name
                    Liaison_Number = SuppliersInfo.Liaison_Number
                    Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
                                    "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
                    Data.append(Supplierinfo)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Purchase_Mgt(request):
    if request.method == "GET":
        PurchaseInfo = procurement.objects.all().order_by('-Purchase_Id')
        Data = []
        try:
            success = True
            if PurchaseInfo:
                if isinstance(PurchaseInfo, Iterable) == True:
                    for Purchase in PurchaseInfo:
                        Purchase_Id = Purchase.Purchase_Id
                        Material_id = Purchase.Material_id
                        Supplier_id = Purchase.Supplier_id
                        Purchase_Date = Purchase.Purchase_Date
                        Purchase_Quantity = Purchase.Purchase_Quantity
                        ResponsibleStaff = Purchase.ResponsibleStaff_id
                        info = {"Purchase_Id": Purchase_Id, "Supplier_id": Supplier_id, "Material_id": Material_id,
                                    "Purchase_Date": Purchase_Date,"Purchase_Quantity":Purchase_Quantity,"ResponsibleStaff":ResponsibleStaff}
                        Data.append(info)
                else:
                    Purchase_Id = PurchaseInfo.Purchase_Id
                    Material_id = PurchaseInfo.Material_id
                    Supplier_id = PurchaseInfo.Supplier_id
                    Purchase_Date = PurchaseInfo.Purchase_Date
                    Purchase_Quantity = PurchaseInfo.Purchase_Quantity
                    ResponsibleStaff = PurchaseInfo.ResponsibleStaff_id
                    info = {"Purchase_Id": Purchase_Id, "Supplier_id": Supplier_id, "Material_id": Material_id,
                            "Purchase_Date": Purchase_Date, "Purchase_Quantity": Purchase_Quantity,
                            "ResponsibleStaff": ResponsibleStaff}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def addPurchase(request):
    if request.method =="POST":
        Data = []
        try:
            success = True
            Material_id = request.POST['materialid']
            Supplier_id = request.POST['supplierid']
            Purchase_Quantity = request.POST['quantity']
            ResponsibleStaff_id = request.POST['staff']
            procurement.objects.create(Material_id=Material_id, Supplier_id=Supplier_id,Purchase_Date=datetime.datetime.now(),Purchase_Quantity=Purchase_Quantity,ResponsibleStaff_id=ResponsibleStaff_id)
            MaterialInfo = material_inventory.objects.get(Material_Id=Material_id)
            Quantity = filter(str.isdigit, Purchase_Quantity.encode("utf-8"))
            Qua = int(Quantity)
            Material_Suplus = Qua+MaterialInfo.Material_Surplus
            Material_inventory.objects.filter(Material_Id=Material_id).update(Material_Surplus=Material_Suplus)#添加
        except Exception as e:
            success = False
            Data = str(e)
        return render(request,'Purchase.html')

def Material_Mgt(request):
    if request.method == "GET":
        MaterialInfo = material_inventory.objects.all()
        Data = []
        try:
            success = True
            if MaterialInfo:
                if isinstance(MaterialInfo, Iterable) == True:
                    for Material in MaterialInfo:
                        Material_Id = Material.Material_Id
                        Material_Name = Material.Material_Name
                        Material_Category = Material.Material_Category
                        Material_Surplus = Material.Material_Surplus
                        Warehouse_id = Material.Warehouse_id
                        info = {"Material_Id": Material_Id, "Material_Name": Material_Name, "Material_Category": Material_Category,
                                    "Material_Surplus": Material_Surplus,"Warehouse_id":Warehouse_id}
                        Data.append(info)
                else:
                    Material_Id = MaterialInfo.Material_Id
                    Material_Name = MaterialInfo.Material_Name
                    Material_Category = MaterialInfo.Material_Category
                    Material_Surplus = MaterialInfo.Material_Surplus
                    Warehouse_id = MaterialInfo.Warehouse_id
                    info = {"Material_Id": Material_Id, "Material_Name": Material_Name,
                            "Material_Category": Material_Category,
                            "Material_Surplus": Material_Surplus, "Warehouse_id": Warehouse_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def addActivity(request):
    if request.method =="POST":
        Data = []
        try:
            success = True
            Product_id = request.POST['Product_id']
            ActResponStaff_id = request.POST['ActResponStaff_id']
            Act_Quantity = request.POST['Act_Quantity']#API请求参数新增 time
            Warehouse_id = request.POST['Warehouse_id']
            Quantity = filter(str.isdigit, Act_Quantity.encode("utf-8"))
            Qua = int(Quantity)
            ProductInfo = product_inventory.objects.get(Product_Id=Product_id)
            Suplus = Qua + ProductInfo.Surplus
            product_inventory.objects.filter(Product_Id=Product_id).update(Surplus=Suplus)  # 添加
            MaterialInfo = material_inventory.objects.get(Material_Id=1)
            Surmine = MaterialInfo.Material_Surplus-Qua*50
            material_inventory.objects.filter(Material_Id=1).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=2)
            Surmine = MaterialInfo.Material_Surplus-Qua*50
            material_inventory.objects.filter(Material_Id=2).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=3)
            Surmine = MaterialInfo.Material_Surplus-Qua*10
            material_inventory.objects.filter(Material_Id=3).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=4)
            Surmine = MaterialInfo.Material_Surplus-Qua*20
            material_inventory.objects.filter(Material_Id=4).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=5)
            Surmine = MaterialInfo.Material_Surplus-Qua*1
            material_inventory.objects.filter(Material_Id=5).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=6)
            Surmine = MaterialInfo.Material_Surplus-Qua*10
            material_inventory.objects.filter(Material_Id=6).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=7)
            Surmine = MaterialInfo.Material_Surplus-Qua*20
            material_inventory.objects.filter(Material_Id=7).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=8)
            Surmine = MaterialInfo.Material_Surplus-Qua*1
            material_inventory.objects.filter(Material_Id=8).update(Material_Surplus=Surmine)
            MaterialInfo = material_inventory.objects.get(Material_Id=9)
            Surmine = MaterialInfo.Material_Surplus-Qua*50
            material_inventory.objects.filter(Material_Id=9).update(Material_Surplus=Surmine)
            production_activity.objects.create(Product_id=Product_id, Act_Date=datetime.datetime.now(),ActResponStaff_id=ActResponStaff_id,Act_Quantity=Act_Quantity,Warehouse_id=Warehouse_id)
        except Exception as e:
            success = False
            Data = str(e)
        return render(request, 'Activity.html')

def Activity_Mgt(request):
    if request.method == "GET":
        ActivityInfo = production_activity.objects.all().order_by('-Activity_Id')
        Data = []
        try:
            success = True
            if ActivityInfo:
                if isinstance(ActivityInfo, Iterable) == True:
                    for Activity in ActivityInfo:
                        Activity_Id = Activity.Activity_Id
                        Product_id = Activity.Product_id
                        Act_Date = Activity.Act_Date
                        Act_Quantity = Activity.Act_Quantity
                        Warehouse_id = Activity.Warehouse_id
                        ActResponStaff_id = Activity.ActResponStaff_id
                        info = {"ActResponStaff_id": ActResponStaff_id, "Act_Quantity": Act_Quantity, "Act_Date": Act_Date,
                                    "Product_id": Product_id,"Warehouse_id":Warehouse_id,"Activity_Id":Activity_Id}
                        Data.append(info)
                else:
                    Activity_Id = ActivityInfo.Activity_Id
                    Product_id = ActivityInfo.Product_id
                    Act_Date = ActivityInfo.Act_Date
                    Act_Quantity = ActivityInfo.Act_Quantity
                    Warehouse_id = ActivityInfo.Warehouse_id
                    ActResponStaff_id = ActivityInfo.ActResponStaff_id
                    info = {"ActResponStaff_id": ActResponStaff_id, "Act_Quantity": Act_Quantity, "Act_Date": Act_Date,
                            "Product_id": Product_id, "Warehouse_id": Warehouse_id, "Activity_Id": Activity_Id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Product_Mgt(request):
    if request.method == "GET":
        ProductInfo = product_inventory.objects.all()
        Data = []
        try:
            success = True
            if ProductInfo:
                if isinstance(ProductInfo, Iterable) == True:
                    for Product in ProductInfo:
                        Product_Id = Product.Product_Id
                        Pro_Category = Product.Pro_Category
                        Warehouse_id = Product.Warehouse_id
                        Surplus = Product.Surplus
                        info = {"Product_Id": Product_Id, "Pro_Category": Pro_Category, "Warehouse_id": Warehouse_id,
                                    "Surplus": Surplus}
                        Data.append(info)
                else:
                    Product_Id = ProductInfo.Product_Id
                    Pro_Category = ProductInfo.Pro_Category
                    Warehouse_id = ProductInfo.Warehouse_id
                    Surplus = ProductInfo.Surplus
                    info = {"Product_Id": Product_Id, "Pro_Category": Pro_Category, "Warehouse_id": Warehouse_id,
                            "Surplus": Surplus}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def addOrder(request):
    if request.method =="POST":
        Data = []
        try:
            success = True
            Customer_id =  request.POST['Customer_id']
            Product_id =  request.POST['Product_id']
            Description =  request.POST['Description']#API请求参数新增 time
            Delivery_Date =  request.POST['Delivery_Date']
            ResponsibleMan_id =  request.POST['ResponsibleMan_id']
            Product_Case =  request.POST['Product_Case']
            Quantity = filter(str.isdigit, Product_Case.encode("utf-8"))
            Qua = int(Quantity)
            OrderInfo = product_inventory.objects.get(Product_Id=Product_id)
            Suplus = OrderInfo.Surplus - Qua
            product_inventory.objects.filter(Product_Id=Product_id).update(Surplus=Suplus)  # 添加
            orders.objects.create(Customer_id=Customer_id, Product_id=Product_id,Description=Description,Delivery_Date=Delivery_Date,ResponsibleMan_id=ResponsibleMan_id,Product_Case=Product_Case,Order_Date=datetime.datetime.now())#返回时间和ID
        except Exception as e:
            success = False
            Data = str(e)
        return render(request, 'Orders.html')

def Order_Mgt(request):
    if request.method == "GET":
        OrderInfo = orders.objects.all().order_by('-Order_Id')
        Data = []
        try:
            success = True
            if OrderInfo:
                if isinstance(OrderInfo, Iterable) == True:
                    for Order in OrderInfo:
                        Order_Id = Order.Order_Id
                        Customer_id = Order.Customer_id
                        Order_Date = Order.Order_Date
                        Product_id = Order.Product_id
                        Product_Case = Order.Product_Case
                        Description = Order.Description
                        Delivery_Date = Order.Delivery_Date
                        ResponsibleMan_id = Order.ResponsibleMan_id
                        info = {"Order_Id": Order_Id, "Customer_id": Customer_id, "Order_Date": Order_Date,
                                    "Product_id": Product_id, "Product_Case": Product_Case, "Description": Description, "Delivery_Date": Delivery_Date,
                                    "ResponsibleMan_id": ResponsibleMan_id}
                        Data.append(info)
                else:
                    Order_Id = OrderInfo.Order_Id
                    Customer_id = OrderInfo.Customer_id
                    Order_Date = OrderInfo.Order_Date
                    Product_id = OrderInfo.Product_id
                    Product_Case = OrderInfo.Product_Case
                    Description = OrderInfo.Description
                    Delivery_Date = OrderInfo.Delivery_Date
                    ResponsibleMan_id = OrderInfo.ResponsibleMan_id
                    info = {"Order_Id": Order_Id, "Customer_id": Customer_id, "Order_Date": Order_Date,
                            "Product_id": Product_id, "Product_Case": Product_Case, "Description": Description,
                            "Delivery_Date": Delivery_Date,
                            "ResponsibleMan_id": ResponsibleMan_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Customer_Mgt(request):
    if request.method == "GET":
        CustomerInfo = customers.objects.all()
        Data = []
        try:
            success = True
            if CustomerInfo:
                if isinstance(CustomerInfo, Iterable) == True:
                    for Customer in CustomerInfo:
                        Customer_Id = Customer.Customer_Id
                        Customer_Name = Customer.Customer_Name
                        Customer_Category = Customer.Customer_Category
                        PhoneNum = Customer.PhoneNum
                        Customer_Address = Customer.Customer_Address
                        info = {"Customer_Id": Customer_Id, "Customer_Name": Customer_Name, "Customer_Category": Customer_Category,
                                    "PhoneNum": PhoneNum, "Customer_Address": Customer_Address}
                        Data.append(info)
                else:
                    Customer_Id = CustomerInfo.Customer_Id
                    Customer_Name = CustomerInfo.Customer_Name
                    Customer_Category = CustomerInfo.Customer_Category
                    PhoneNum = CustomerInfo.PhoneNum
                    Customer_Address = CustomerInfo.Customer_Address
                    info = {"Customer_Id": Customer_Id, "Customer_Name": Customer_Name,
                            "Customer_Category": Customer_Category,
                            "PhoneNum": PhoneNum, "Customer_Address": Customer_Address}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Equipment_Mgt(request):
    if request.method == "GET":
        EquipmentInfo = equipments.objects.all()
        Data = []
        try:
            success = True
            if EquipmentInfo:
                if isinstance(EquipmentInfo, Iterable) == True:
                    for Equipment in EquipmentInfo:
                        Equip_Id = Equipment.Equip_Id
                        Equip_Name = Equipment.Equip_Name
                        Warehouse_id = Equipment.Warehouse_id
                        info = {"Equip_Id": Equip_Id, "Equip_Name": Equip_Name, "Warehouse_id": Warehouse_id}
                        Data.append(info)
                else:
                    Equip_Id = EquipmentInfo.Equip_Id
                    Equip_Name = EquipmentInfo.Equip_Name
                    Warehouse_id = EquipmentInfo.Warehouse_id
                    info = {"Equip_Id": Equip_Id, "Equip_Name": Equip_Name, "Warehouse_id": Warehouse_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Maintenances_Mgt(request):
    if request.method == "GET":
        MaintenanceInfo = maintenances.objects.all()
        Data = []
        try:
            success = True
            if MaintenanceInfo:
                if isinstance(MaintenanceInfo, Iterable) == True:
                    for Maintenance in MaintenanceInfo:
                        Mainten_Id = Maintenance.Mainten_Id
                        Mainten_Date = Maintenance.Mainten_Date
                        Equip_id = Maintenance.Equip_id
                        Deprecation = Maintenance.Deprecation
                        MaintenStaff_id = Maintenance.MaintenStaff_id
                        info = {"Mainten_Id": Mainten_Id, "Mainten_Date": Mainten_Date, "Equip_id": Equip_id, "Deprecation": Deprecation, "MaintenStaff_id": MaintenStaff_id}
                        Data.append(info)
                else:
                    Mainten_Id = MaintenanceInfo.Mainten_Id
                    Mainten_Date = MaintenanceInfo.Mainten_Date
                    Equip_id = MaintenanceInfo.Equip_id
                    Deprecation = MaintenanceInfo.Deprecation
                    MaintenStaff_id = MaintenanceInfo.MaintenStaff_id
                    info = {"Mainten_Id": Mainten_Id, "Mainten_Date": Mainten_Date, "Equip_id": Equip_id,
                            "Deprecation": Deprecation, "MaintenStaff_id": MaintenStaff_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Warehouse_Mgt(request):
    if request.method == "GET":
        WarehouseInfo = warehouse.objects.all()
        Data = []
        try:
            success = True
            if WarehouseInfo:
                if isinstance(WarehouseInfo, Iterable) == True:
                    for House in WarehouseInfo:
                        Warehouse_Id = House.Warehouse_Id
                        Storage_Type = House.Storage_Type
                        Warehouse_Location = House.Warehouse_Location
                        PeopleInCharge_id = House.PeopleInCharge_id
                        info = {"Warehouse_Id": Warehouse_Id, "Storage_Type": Storage_Type, "Warehouse_Location": Warehouse_Location, "PeopleInCharge_id": PeopleInCharge_id}
                        Data.append(info)
                else:
                    Warehouse_Id = WarehouseInfo.Warehouse_Id
                    Storage_Type = WarehouseInfo.Storage_Type
                    Warehouse_Location = WarehouseInfo.Warehouse_Location
                    PeopleInCharge_id = WarehouseInfo.PeopleInCharge_id
                    info = {"Warehouse_Id": Warehouse_Id, "Storage_Type": Storage_Type,
                            "Warehouse_Location": Warehouse_Location, "PeopleInCharge_id": PeopleInCharge_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Labor_Mgt(request):
    if request.method == "GET":
        StaffInfo = staff.objects.all()
        Data = []
        try:
            success = True
            if StaffInfo:
                if isinstance(StaffInfo, Iterable) == True:
                    for Labor in StaffInfo:
                        WorkNum = Labor.WorkNum
                        Staff_Name = Labor.Staff_Name
                        Department = Labor.Department
                        Staff_Gender = Labor.Staff_Gender
                        info = {"WorkNum": WorkNum, "Staff_Name": Staff_Name, "Department": Department, "Staff_Gender": Staff_Gender}
                        Data.append(info)
                else:
                    WorkNum = StaffInfo.WorkNum
                    Staff_Name = StaffInfo.Staff_Name
                    Department = StaffInfo.Department
                    Staff_Gender = StaffInfo.Staff_Gender
                    info = {"WorkNum": WorkNum, "Staff_Name": Staff_Name, "Department": Department,
                            "Staff_Gender": Staff_Gender}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def Main_Mgt(request):
    if request.method == "GET":
        MainInfo = maintenances.objects.all().order_by('-Mainten_Id')
        Data = []
        try:
            success = True
            if MainInfo:
                if isinstance(MainInfo, Iterable) == True:
                    for Labor in MainInfo:
                        Mainten_Id = Labor.Mainten_Id
                        Mainten_Date = Labor.Mainten_Date
                        Deprecation = Labor.Deprecation
                        Equip_id = Labor.Equip_id
                        MaintenStaff_id = Labor.MaintenStaff_id
                        info = {"Mainten_Id": Mainten_Id, "Mainten_Date": Mainten_Date, "Deprecation": Deprecation, "Equip_id": Equip_id,"MaintenStaff_id":MaintenStaff_id}
                        Data.append(info)
                else:
                    Mainten_Id = MainInfo.Mainten_Id
                    Mainten_Date = MainInfo.Mainten_Date
                    Deprecation = MainInfo.Deprecation
                    Equip_id = MainInfo.Equip_id
                    MaintenStaff_id = MainInfo.MaintenStaff_id
                    info = {"Mainten_Id": Mainten_Id, "Mainten_Date": Mainten_Date, "Deprecation": Deprecation,
                            "Equip_id": Equip_id, "MaintenStaff_id": MaintenStaff_id}
                    Data.append(info)
            else:
                pass
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def addMaintenance(request):
    if request.method =="POST":
        Data = []
        try:
            success = True
            Equipmentid =  request.POST['Equipmentid']
            Description =  request.POST['Description']
            MaintenStaffid =  request.POST['MaintenStaffid']
            maintenances.objects.create(Mainten_Date=datetime.datetime.now(),Equip_id=Equipmentid, Deprecation=Description,MaintenStaff_id=MaintenStaffid)
        except Exception as e:
            success = False
            Data = str(e)
        return render(request, 'Maintenance.html')

def getSupplier(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Supplier_Id =  request.GET['Supplier_Id']
            Supplier_Name =  request.GET['Supplier_Name']
            Material_id =  request.GET['Material_id']
            Liaison_Number = request.GET['Liaison_Number']
            Liaison_Name = request.GET['Liaison_Name']
            search_dict = dict()
            if Supplier_Id:
                search_dict['Supplier_Id'] = Supplier_Id
            if Supplier_Name:
                search_dict['Supplier_Name'] = Supplier_Name
            if Material_id:
                search_dict['Material_id'] = Material_id
            if Liaison_Number:
                search_dict['Liaison_Number'] = Liaison_Number
            if Liaison_Name:
                search_dict['Liaison_Name'] = Liaison_Name
            Info = suppliers.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Supplier in Info:
                        Supplier_Id = Supplier.Supplier_Id
                        Supplier_Name = Supplier.Supplier_Name
                        Material_id = Supplier.Material_id
                        Liaison_Name = Supplier.Liaison_Name
                        Liaison_Number = Supplier.Liaison_Number
                        Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
                                    "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
                        Data.append(Supplierinfo)
                else:
                    Supplier_Id = Info.Supplier_Id
                    Supplier_Name = Info.Supplier_Name
                    Material_id = Info.Material_id
                    Liaison_Name = Info.Liaison_Name
                    Liaison_Number = Info.Liaison_Number
                    Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
                                    "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
                    Data.append(Supplierinfo)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getPurchase(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Purchase_Id =  request.GET['Purchase_Id']
            Purchase_Date =  request.GET['Purchase_Date']
            Material_id =  request.GET['Material_id']
            Supplier_id = request.GET['Supplier_id']
            search_dict = dict()
            if Purchase_Id:
                search_dict['Purchase_Id'] = Purchase_Id
            if Purchase_Date:
                search_dict['Purchase_Date'] = Purchase_Date
            if Material_id:
                search_dict['Material_id'] = Material_id
            if Supplier_id:
                search_dict['Supplier_id'] = Supplier_id
            if Supplier_id:
                search_dict['Supplier_id'] = Supplier_id
            Info = procurement.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Purchase in Info:
                        Purchase_Id = Purchase.Purchase_Id
                        Material_id = Purchase.Material_id
                        Supplier_id = Purchase.Supplier_id
                        Purchase_Date = Purchase.Purchase_Date
                        Purchase_Quantity = Purchase.Purchase_Quantity
                        ResponsibleStaff = Purchase.ResponsibleStaff_id
                        info = {"Purchase_Id": Purchase_Id, "Supplier_id": Supplier_id, "Material_id": Material_id,
                                    "Purchase_Date": Purchase_Date,"Purchase_Quantity":Purchase_Quantity,"ResponsibleStaff":ResponsibleStaff}
                        Data.append(info)
                else:
                    Purchase_Id = Info.Purchase_Id
                    Material_id = Info.Material_id
                    Supplier_id = Info.Supplier_id
                    Purchase_Date = Info.Purchase_Date
                    Purchase_Quantity = Info.Purchase_Quantity
                    ResponsibleStaff = Info.ResponsibleStaff_id
                    info = {"Purchase_Id": Purchase_Id, "Supplier_id": Supplier_id, "Material_id": Material_id,
                            "Purchase_Date": Purchase_Date, "Purchase_Quantity": Purchase_Quantity,
                            "ResponsibleStaff": ResponsibleStaff}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getMaterial(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Material_Id =  request.GET['Material_Id']
            Material_Name =  request.GET['Material_Name']
            Material_Category =  request.GET['Material_Category']
            Warehouse_id = request.GET['Warehouse_id']
            search_dict = dict()
            if Material_Id:
                search_dict['Material_Id'] = Material_Id
            if Material_Name:
                search_dict['Material_Name'] = Material_Name
            if Material_Category:
                search_dict['Material_Category'] = Material_Category
            if Warehouse_id:
                search_dict['Warehouse_id'] = Warehouse_id
            Info = material_inventory.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Material in Info:
                        Material_Id = Material.Material_Id
                        Material_Name = Material.Material_Name
                        Material_Category = Material.Material_Category
                        Material_Surplus = Material.Material_Surplus
                        Warehouse_id = Material.Warehouse_id
                        info = {"Material_Id": Material_Id, "Material_Name": Material_Name, "Material_Category": Material_Category,
                                    "Material_Surplus": Material_Surplus,"Warehouse_id":Warehouse_id}
                        Data.append(info)
                else:
                    Material_Id = Info.Material_Id
                    Material_Name = Info.Material_Name
                    Material_Category = Info.Material_Category
                    Material_Surplus = Info.Material_Surplus
                    Warehouse_id = Info.Warehouse_id
                    info = {"Material_Id": Material_Id, "Material_Name": Material_Name,
                            "Material_Category": Material_Category,
                            "Material_Surplus": Material_Surplus, "Warehouse_id": Warehouse_id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getActivity(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Activity_Id =  request.GET['Activity_Id']
            Warehouse_id =  request.GET['Warehouse_id']
            Product_id =  request.GET['Product_id']
            ActResponStaff_id = request.GET['ActResponStaff_id']
            search_dict = dict()
            if Activity_Id:
                search_dict['Activity_Id'] = Activity_Id
            if Warehouse_id:
                search_dict['Warehouse_id'] = Warehouse_id
            if Product_id:
                search_dict['Product_id'] = Product_id
            if ActResponStaff_id:
                search_dict['ActResponStaff_id'] = ActResponStaff_id
            Info = production_activity.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Activity in Info:
                        Activity_Id = Activity.Activity_Id
                        Product_id = Activity.Product_id
                        Act_Date = Activity.Act_Date
                        Act_Quantity = Activity.Act_Quantity
                        Warehouse_id = Activity.Warehouse_id
                        ActResponStaff_id = Activity.ActResponStaff_id
                        info = {"ActResponStaff_id": ActResponStaff_id, "Act_Quantity": Act_Quantity, "Act_Date": Act_Date,
                                    "Product_id": Product_id,"Warehouse_id":Warehouse_id,"Activity_Id":Activity_Id}
                        Data.append(info)
                else:
                    Activity_Id = Info.Activity_Id
                    Product_id = Info.Product_id
                    Act_Date = Info.Act_Date
                    Act_Quantity = Info.Act_Quantity
                    Warehouse_id = Info.Warehouse_id
                    ActResponStaff_id = Info .ActResponStaff_id
                    info = {"ActResponStaff_id": ActResponStaff_id, "Act_Quantity": Act_Quantity, "Act_Date": Act_Date,
                            "Product_id": Product_id, "Warehouse_id": Warehouse_id, "Activity_Id": Activity_Id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getOrder(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Order_Id =  request.GET['Order_Id']
            Customer_id =  request.GET['Customer_id']
            Product_id =  request.GET['Product_id']
            ResponsibleMan_id = request.GET['ResponsibleMan_id']
            search_dict = dict()
            if Order_Id:
                search_dict['Order_Id'] = Order_Id
            if Customer_id:
                search_dict['Customer_id'] = Customer_id
            if Product_id:
                search_dict['Product_id'] = Product_id
            if ResponsibleMan_id:
                search_dict['ResponsibleMan_id'] = ResponsibleMan_id
            Info = orders.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Order in Info:
                        Order_Id = Order.Order_Id
                        Customer_id = Order.Customer_id
                        Order_Date = Order.Order_Date
                        Product_id = Order.Product_id
                        Product_Case = Order.Product_Case
                        Description = Order.Description
                        Delivery_Date = Order.Delivery_Date
                        ResponsibleMan_id = Order.ResponsibleMan_id
                        info = {"Order_Id": Order_Id, "Customer_id": Customer_id, "Order_Date": Order_Date,
                                    "Product_id": Product_id, "Product_Case": Product_Case, "Description": Description, "Delivery_Date": Delivery_Date,
                                    "ResponsibleMan_id": ResponsibleMan_id}
                        Data.append(info)
                else:
                    Order_Id = Info.Order_Id
                    Customer_id = Info.Customer_id
                    Order_Date = Info.Order_Date
                    Product_id = Info.Product_id
                    Product_Case = Info.Product_Case
                    Description = Info.Description
                    Delivery_Date = Info.Delivery_Date
                    ResponsibleMan_id = Info.ResponsibleMan_id
                    info = {"Order_Id": Order_Id, "Customer_id": Customer_id, "Order_Date": Order_Date,
                            "Product_id": Product_id, "Product_Case": Product_Case, "Description": Description,
                            "Delivery_Date": Delivery_Date,
                            "ResponsibleMan_id": ResponsibleMan_id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getCustomer(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Customer_Id =  request.GET['Customer_Id']
            Customer_Name =  request.GET['Customer_Name']
            Customer_Category =  request.GET['Customer_Category']
            PhoneNum = request.GET['PhoneNum']
            search_dict = dict()
            if Customer_Id:
                search_dict['Customer_Id'] = Customer_Id
            if Customer_Name:
                search_dict['Customer_Name'] = Customer_Name
            if Customer_Category:
                search_dict['Customer_Category'] = Customer_Category
            if PhoneNum:
                search_dict['PhoneNum'] = PhoneNum
            Info = customers.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Customer in Info:
                        Customer_Id = Customer.Customer_Id
                        Customer_Name = Customer.Customer_Name
                        Customer_Category = Customer.Customer_Category
                        PhoneNum = Customer.PhoneNum
                        Customer_Address = Customer.Customer_Address
                        info = {"Customer_Id": Customer_Id, "Customer_Name": Customer_Name, "Customer_Category": Customer_Category,
                                    "PhoneNum": PhoneNum, "Customer_Address": Customer_Address}
                        Data.append(info)
                else:
                    Customer_Id = Info.Customer_Id
                    Customer_Name = Info.Customer_Name
                    Customer_Category = Info.Customer_Category
                    PhoneNum = Info.PhoneNum
                    Customer_Address = Info.Customer_Address
                    info = {"Customer_Id": Customer_Id, "Customer_Name": Customer_Name,
                            "Customer_Category": Customer_Category,
                            "PhoneNum": PhoneNum, "Customer_Address": Customer_Address}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})


def getMaintenance(request):
    if request.method == "GET":
        Data = []
        try:
            success = True
            Mainten_Id = request.GET['Mainten_Id']
            MaintenStaff_id = request.GET['MaintenStaff_id']
            Equip_id = request.GET['Equip_id']
            search_dict = dict()
            if Mainten_Id:
                search_dict['Mainten_Id'] = Mainten_Id
            if MaintenStaff_id:
                search_dict['MaintenStaff_id'] = MaintenStaff_id
            if Equip_id:
                search_dict['Equip_id'] = Equip_id
            Info = maintenances.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for House in Info:
                        Mainten_Id = House.Mainten_Id
                        MaintenStaff_id = House.MaintenStaff_id
                        Equip_id = House.Equip_id
                        info = {"Mainten_Id": Mainten_Id, "MaintenStaff_id": MaintenStaff_id,
                                "Equip_id": Equip_id}
                        Data.append(info)
                else:
                    Mainten_Id = Info.Mainten_Id
                    MaintenStaff_id = Info.MaintenStaff_id
                    Equip_id = Info.Equip_id
                    info = {"Mainten_Id": Mainten_Id, "MaintenStaff_id": MaintenStaff_id,
                            "Equip_id": Equip_id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getEquipment(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Equip_Id =  request.GET['Equip_Id']
            Equip_Name =  request.GET['Equip_Name']
            Warehouse_id =  request.GET['Warehouse_id']
            search_dict = dict()
            if Equip_Id:
                search_dict['Equip_Id'] = Equip_Id
            if Equip_Name:
                search_dict['Equip_Name'] = Equip_Name
            if Warehouse_id:
                search_dict['Warehouse_id'] = Warehouse_id
            Info = equipments.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Equipment in Info:
                        Equip_Id = Equipment.Equip_Id
                        Equip_Name = Equipment.Equip_Name
                        Warehouse_id = Equipment.Warehouse_id
                        info = {"Equip_Id": Equip_Id, "Equip_Name": Equip_Name, "Warehouse_id": Warehouse_id}
                        Data.append(info)
                else:
                    Equip_Id = Info.Equip_Id
                    Equip_Name = Info.Equip_Name
                    Warehouse_id = Info.Warehouse_id
                    info = {"Equip_Id": Equip_Id, "Equip_Name": Equip_Name, "Warehouse_id": Warehouse_id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getWarehouse(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            Warehouse_Id =  request.GET['Warehouse_Id']
            Storage_Type =  request.GET['Storage_Type']
            Warehouse_Location =  request.GET['Warehouse_Location']
            PeopleInCharge_id = request.GET['PeopleInCharge_id']
            search_dict = dict()
            if Warehouse_Id:
                search_dict['Warehouse_Id'] = Warehouse_Id
            if Storage_Type:
                search_dict['Storage_Type'] = Storage_Type
            if Warehouse_Location:
                search_dict['Warehouse_Location'] = Warehouse_Location
            if PeopleInCharge_id:
                search_dict['PeopleInCharge_id'] = PeopleInCharge_id
            Info = warehouse.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for House in Info:
                        Warehouse_Id = House.Warehouse_Id
                        Storage_Type = House.Storage_Type
                        Warehouse_Location = House.Warehouse_Location
                        PeopleInCharge_id = House.PeopleInCharge_id
                        info = {"Warehouse_Id": Warehouse_Id, "Storage_Type": Storage_Type, "Warehouse_Location": Warehouse_Location, "PeopleInCharge_id": PeopleInCharge_id}
                        Data.append(info)
                else:
                    Warehouse_Id = Info.Warehouse_Id
                    Storage_Type = Info.Storage_Type
                    Warehouse_Location = Info.Warehouse_Location
                    PeopleInCharge_id = Info.PeopleInCharge_id
                    info = {"Warehouse_Id": Warehouse_Id, "Storage_Type": Storage_Type,
                            "Warehouse_Location": Warehouse_Location, "PeopleInCharge_id": PeopleInCharge_id}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getLabor(request):
    if request.method =="GET":
        Data = []
        try:
            success = True
            WorkNum =  request.GET['WorkNum']
            Staff_Name =  request.GET['Staff_Name']
            Department =  request.GET['Department']
            Staff_Gender = request.GET['Staff_Gender']
            search_dict = dict()
            if WorkNum:
                search_dict['WorkNum'] = WorkNum
            if Staff_Name:
                search_dict['Staff_Name'] = Staff_Name
            if Department:
                search_dict['Department'] = Department
            if Staff_Gender:
                search_dict['Staff_Gender'] = Staff_Gender
            Info = staff.objects.filter(**search_dict)
            if Info:
                if isinstance(Info, Iterable) == True:
                    for Labor in Info:
                        WorkNum = Labor.WorkNum
                        Staff_Name = Labor.Staff_Name
                        Department = Labor.Department
                        Staff_Gender = Labor.Staff_Gender
                        info = {"WorkNum": WorkNum, "Staff_Name": Staff_Name, "Department": Department, "Staff_Gender": Staff_Gender}
                        Data.append(info)
                else:
                    WorkNum = Info.WorkNum
                    Staff_Name = Info.Staff_Name
                    Department = Info.Department
                    Staff_Gender = Info.Staff_Gender
                    info = {"WorkNum": WorkNum, "Staff_Name": Staff_Name, "Department": Department,
                            "Staff_Gender": Staff_Gender}
                    Data.append(info)
        except Exception as e:
            success = False
            Data = str(e)
        return JsonResponse({"success": success, "data": Data})

def getDashboard(request):
    if request.method == "GET":
        SupplierNum = suppliers.objects.all().__len__()
        MaterialNum = material_inventory.objects.all().__len__()
        ProductNum = product_inventory.objects.all().__len__()
        OrderNum = orders.objects.all().__len__()
        WarehouseNum = warehouse.objects.all().__len__()
        ActivityNum = production_activity.objects.all().__len__()
        MaterialInfo = material_inventory.objects.all()
        SurplusList = []
        for Material in MaterialInfo:
            Surplus = Material.Material_Surplus
            SurplusList.append(Surplus)
        OrderInfo1 = orders.objects.filter(Product_id=1)
        OrderInfo2 = orders.objects.filter(Product_id=2)
        OrderInfo3 = orders.objects.filter(Product_id=3)
        OrderInfo4 = orders.objects.filter(Product_id=4)
        if OrderInfo1:
            Count = 0
            if isinstance(OrderInfo1, Iterable) == True:
                for Order in OrderInfo1:
                    Product_Case = Order.Product_Case
                    Count = Product_Case+Count
                Count1=Count
            else:
                Count1=1
        else:
            Count1=0

        if OrderInfo2:
            Count = 0
            if isinstance(OrderInfo2, Iterable) == True:
                for Order in OrderInfo2:
                    Product_Case = Order.Product_Case
                    Count = Product_Case+Count
                Count2=Count
            else:
                Count2=1
        else:
            Count2=0

        if OrderInfo3:
            Count = 0
            if isinstance(OrderInfo3, Iterable) == True:
                for Order in OrderInfo3:
                    Product_Case = Order.Product_Case
                    Count = Product_Case+Count
                Count3=Count
            else:
                Count3=1
        else:
            Count3=0

        if OrderInfo4:
            Count = 0
            if isinstance(OrderInfo4, Iterable) == True:
                for Order in OrderInfo4:
                    Product_Case = Order.Product_Case
                    Count = Product_Case+Count
                Count4=Count
            else:
                Count4=1
        else:
            Count4=0
        CountList = [Count1,Count2,Count3,Count4]
        Data = {"SupplierNum":SupplierNum,"MaterialNum":MaterialNum,"ProductNum":ProductNum,"OrderNum":OrderNum,"WarehouseNum":WarehouseNum,"ActivityNum":ActivityNum,"Count":CountList,"Surplus":SurplusList}

        return JsonResponse(Data)
        # Data = []
        # try:
        #     success = True
        #     if SuppliersInfo:
        #         if isinstance(SuppliersInfo, Iterable) == True:
        #             for Supplier in SuppliersInfo:
        #                 Supplier_Id = Supplier.Supplier_Id
        #                 Supplier_Name = Supplier.Supplier_Name
        #                 Material_id = Supplier.Material_id
        #                 Liaison_Name = Supplier.Liaison_Name
        #                 Liaison_Number = Supplier.Liaison_Number
        #                 Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
        #                             "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
        #                 Data.append(Supplierinfo)
        #         else:
        #             Supplier_Id = SuppliersInfo.Supplier_Id
        #             Supplier_Name = SuppliersInfo.Supplier_Name
        #             Material_id = SuppliersInfo.Material_id
        #             Liaison_Name = SuppliersInfo.Liaison_Name
        #             Liaison_Number = SuppliersInfo.Liaison_Number
        #             Supplierinfo = {"Liaison_Number": Liaison_Number, "Liaison_Name": Liaison_Name, "Material_id": Material_id,
        #                             "Supplier_Name": Supplier_Name,"Supplier_Id":Supplier_Id}
        #             Data.append(Supplierinfo)
        #     else:
        #         pass
        # except Exception as e:
        #     success = False
        #     Data = str(e)
        # return JsonResponse({"success": success, "data": Data})
