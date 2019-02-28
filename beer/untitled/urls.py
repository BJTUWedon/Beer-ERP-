from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from Beer.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^login$', login, name='login'),
    url(r'^home', home, name='home'),
    url(r'^SupplierMgt$', Supplier_Mgt, name='SupplierMgt'),
    url(r'^Supplier', Supplier),
    url(r'^Purchase', Purchase),
    url(r'^MgtPurchase$', Purchase_Mgt),
    url(r'^Material', Material),
    url(r'^MgtMaterial$', Material_Mgt),
    url(r'^Activity', Activity),
    url(r'^MgtActivity$', Activity_Mgt),
    url(r'^Product', Product),
    url(r'^MgtProduct$', Product_Mgt),
    url(r'^Orders', Orders1),
    url(r'^MgtOrders$', Order_Mgt),
    url(r'^Customers', Customers1),
    url(r'^MgtCustomers$', Customer_Mgt),
    url(r'^Equipment', Equipment),
    url(r'^MgtEquipment$', Equipment_Mgt),
    url(r'^Warehouse', Warehouse1),
    url(r'^MgtWarehouse$', Warehouse_Mgt),
    url(r'^MgtLabor$', Labor_Mgt),
    url(r'^Labor', Labor),
    url(r'^Tem_addPurchase', Tem_addPurchase),
    url(r'^Tem_addOrder', Tem_addOrder),
    url(r'^addOrder', addOrder, name='addOrder'),
    url(r'^addPurchase', addPurchase,name='addPurchase'),
    url(r'^addActivity', addActivity,name='addActivity'),
    url(r'^Tem_addActivity', Tem_addActivity),
    url(r'^Maintenance', Maintenance),
    url(r'^MgtMaintenance$', Main_Mgt),
    url(r'^Tem_addMaintenance', Tem_addMaintenance),
    url(r'^addMaintenance', addMaintenance,name='addMaintenance'),
    url(r'^getSupplier', getSupplier,name='getSupplier'),
    url(r'^getPurchase', getPurchase,name='getPurchase'),
    url(r'^getMaterial', getMaterial,name='getMaterial'),
    url(r'^getActivity', getActivity,name='getActivity'),
    url(r'^getOrder', getOrder, name='getOrder'),
    url(r'^getCustomer', getCustomer, name='getCustomer'),
    url(r'^getEquipment', getEquipment, name='getEquipment'),
    url(r'^getWarehouse', getWarehouse, name='getWarehouse'),
    url(r'^getLabor', getLabor, name='getLabor'),
    url(r'^Dashboard', Dashboard, name='Dashboard'),
    url(r'^getDashboard', getDashboard, name='getDashboard'),
    url(r'^getMaintenance', getMaintenance, name='getMaintenance'),











]