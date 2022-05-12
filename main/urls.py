from django.urls import path
from .views import home, getAllItems, addItem, addBill, Register, updateItems, getPdf

urlpatterns = [
    path('',home,name='home'),
    path('getAllItems/',getAllItems,name="Getallitems"),
    path('addItem/',addItem,name="Additem"),
    path('register/',Register,name="Register"),
    path('addBill/',addBill,name="Addbill"),
    path('updateItem/',updateItems,name="UpdateItem"),
    path('getPdf/',getPdf,name="GetPdf"),
]
