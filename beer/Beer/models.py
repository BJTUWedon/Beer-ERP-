from django.db import models

# Create your models here.

class staff(models.Model):
    WorkNum = models.AutoField(primary_key=True)
    Staff_Name = models.CharField(max_length=128)
    Department = models.CharField(max_length=128)
    Staff_Gender = models.CharField(max_length=64)

class administrators(models.Model):
    Admin_Id = models.AutoField(primary_key=True)
    WorkNum = models.ForeignKey(Staff)
    Admin_Username = models.CharField(max_length=128)
    Admin_Password = models.CharField(max_length=128)

class warehouse(models.Model):
    Warehouse_Id = models.AutoField(primary_key=True)
    Storage_Type = models.CharField(max_length=128)
    Warehouse_Location = models.CharField(max_length=128)
    PeopleInCharge = models.ForeignKey(Staff)

class material_inventory(models.Model):
    Material_Id = models.AutoField(primary_key=True)
    Material_Name = models.CharField(max_length=128)
    Material_Category = models.CharField(max_length=128)
    Material_Surplus = models.IntegerField()
    Warehouse = models.ForeignKey(Warehouse)

class suppliers(models.Model):
    Supplier_Id = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=128)
    Material = models.ForeignKey(Material_Inventory)
    Liaison_Name = models.CharField(max_length=128)
    Liaison_Number = models.IntegerField()

class procurement(models.Model):
    Purchase_Id = models.AutoField(primary_key=True)
    Material = models.ForeignKey(Material_Inventory)
    Supplier = models.ForeignKey(Suppliers)
    Purchase_Date = models.DateField()
    Purchase_Quantity = models.IntegerField()
    ResponsibleStaff = models.ForeignKey(Staff,default="")

class product_inventory(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Pro_Category = models.CharField(max_length=128)
    Warehouse = models.ForeignKey(Warehouse)
    Surplus = models.IntegerField()

class customers(models.Model):
    Customer_Id = models.AutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=128)
    Customer_Category = models.CharField(max_length=128)
    PhoneNum = models.IntegerField()
    Customer_Address = models.CharField(max_length=250)

class orders(models.Model):
    Order_Id = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(Customers)
    Order_Date = models.DateField()
    Product = models.ForeignKey(Product_Inventory)
    Product_Case = models.IntegerField()
    Description = models.CharField(max_length=250)
    Delivery_Date = models.DateField()
    ResponsibleMan = models.ForeignKey(Staff)

class equipments(models.Model):
    Equip_Id = models.AutoField(primary_key=True)
    Equip_Name = models.CharField(max_length=128)
    Warehouse = models.ForeignKey(Warehouse)

class maintenances(models.Model):
    Mainten_Id = models.AutoField(primary_key=True)
    Mainten_Date = models.DateField()
    Equip = models.ForeignKey(Equipments)
    Deprecation = models.CharField(max_length=250)
    MaintenStaff = models.ForeignKey(Staff)

class production_activity(models.Model):
    Activity_Id = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product_Inventory)
    Act_Date = models.DateField()
    Act_Quantity = models.IntegerField()
    Warehouse = models.ForeignKey(Warehouse)
    ActResponStaff = models.ForeignKey(Staff)
