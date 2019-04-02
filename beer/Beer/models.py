from django.db import models

# Create your models here.

class staff(models.Model):
    WorkNum = models.AutoField(primary_key=True)
    Staff_Name = models.CharField(max_length=128)
    Department = models.CharField(max_length=128)
    Staff_Gender = models.CharField(max_length=64)

class administrators(models.Model):
    Admin_Id = models.AutoField(primary_key=True)
    WorkNum = models.ForeignKey(staff)
    Admin_Username = models.CharField(max_length=128)
    Admin_Password = models.CharField(max_length=128)

class warehouse(models.Model):
    Warehouse_Id = models.AutoField(primary_key=True)
    Storage_Type = models.CharField(max_length=128)
    Warehouse_Location = models.CharField(max_length=128)
    PeopleInCharge = models.ForeignKey(staff)

class material_inventory(models.Model):
    Material_Id = models.AutoField(primary_key=True)
    Material_Name = models.CharField(max_length=128)
    Material_Category = models.CharField(max_length=128)
    Material_Surplus = models.IntegerField()
    Warehouse = models.ForeignKey(warehouse)

class suppliers(models.Model):
    Supplier_Id = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=128)
    Material = models.ForeignKey(material_inventory)
    Liaison_Name = models.CharField(max_length=128)
    Liaison_Number = models.IntegerField()

class procurement(models.Model):
    Purchase_Id = models.AutoField(primary_key=True)
    Material = models.ForeignKey(material_inventory)
    Supplier = models.ForeignKey(suppliers)
    Purchase_Date = models.DateField()
    Purchase_Quantity = models.IntegerField()
    ResponsibleStaff = models.ForeignKey(staff,default="")

class product_inventory(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Pro_Category = models.CharField(max_length=128)
    Warehouse = models.ForeignKey(warehouse)
    Surplus = models.IntegerField()

class customers(models.Model):
    Customer_Id = models.AutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=128)
    Customer_Category = models.CharField(max_length=128)
    PhoneNum = models.IntegerField()
    Customer_Address = models.CharField(max_length=250)

class orders(models.Model):
    Order_Id = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(customers)
    Order_Date = models.DateField()
    Product = models.ForeignKey(product_inventory)
    Product_Case = models.IntegerField()
    Description = models.CharField(max_length=250)
    Delivery_Date = models.DateField()
    ResponsibleMan = models.ForeignKey(staff)

class equipments(models.Model):
    Equip_Id = models.AutoField(primary_key=True)
    Equip_Name = models.CharField(max_length=128)
    Warehouse = models.ForeignKey(warehouse)

class maintenances(models.Model):
    Mainten_Id = models.AutoField(primary_key=True)
    Mainten_Date = models.DateField()
    Equip = models.ForeignKey(equipments)
    Deprecation = models.CharField(max_length=250)
    MaintenStaff = models.ForeignKey(staff)

class production_activity(models.Model):
    Activity_Id = models.AutoField(primary_key=True)
    Product = models.ForeignKey(product_inventory)
    Act_Date = models.DateField()
    Act_Quantity = models.IntegerField()
    Warehouse = models.ForeignKey(warehouse)
    ActResponStaff = models.ForeignKey(staff)
