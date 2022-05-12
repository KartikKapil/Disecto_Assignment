from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from numpy import product
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth.models import User
from main.models import Customer, Product, Bill
from .serialzier import CustomerSerializer, ProductSerializer, BillSerializer
from rest_framework.response import Response
from reportlab.pdfgen import canvas  


@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def addItem(request):
    """ Returns Newly added object or Error"""


    new_item = ProductSerializer(data=request.data)
    if new_item.is_valid():
        new_item.save()
        return Response(new_item.data,status=status.HTTP_201_CREATED)
    return Response({
        'error': new_item.errors,
    })

@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def Register(request):
    """ Returns Newly added User or Error"""


    customer_serializer = CustomerSerializer(data=request.data)
    if customer_serializer.is_valid():
        customer_serializer.save()
        if customer_serializer.is_valid():
            print("working")
            # customer_serializer.save()
        return Response(customer_serializer.data,status=status.HTTP_201_CREATED)
    return Response({
        'error': customer_serializer.errors,
    })

@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def getAllItems(request):
    """ Returns a list of all the product """


    prod_list = Product.objects.all()
    serialized_data = ProductSerializer(prod_list,many=True)
    return Response(serialized_data.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def addBill(request):
    """ Returns Newly added object or Error"""


    username = request.data['username']
    user = User.objects.get(username=username)
    customer = Customer.objects.get(user=user)
    list_of_objects = request.data['list_of_objects']
    for obj in list_of_objects:
        name_of_item = list(obj)[0]
        quantity = obj[name_of_item]
        try :
            item = Product.objects.get(name=name_of_item)
        except Product.ObjectDoesNotExist:
            return HttpResponse("Kindly Add All items")

        price = quantity*item.price
        bill = Bill(customer=customer,product=item,quantity=quantity,price=price)
        bill.save()
    return HttpResponse("Bill Generated")

@api_view(['POSt'])
@permission_classes((permissions.AllowAny, ))
def updateItems(request):
    username = request.data['username']
    user = User.objects.get(username=username)
    customer = Customer.objects.get(user=user)
    list_of_objects = request.data['list_of_objects']
    for obj in list_of_objects:
        name_of_item = list(obj)[0]
        quantity = obj[name_of_item]
        item = Product.objects.get(name=name_of_item)
        bill = Bill.objects.get(customer=customer,product=item)
        bill.quantity = quantity
        bill.price = item.price * quantity
        bill.save()
    
    return HttpResponse("Updated Bill")

@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def getPdf(request):
    username = request.GET['username']
    user = User.objects.get(username=username)
    customer = Customer.objects.get(user=user)
    bill_list = Bill.objects.filter(customer=customer)
    List_of_items = []
    for bill in bill_list:
        List_of_items.append([bill.product.name,bill.quantity,bill.price])
    
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 12)  
    p.drawString(110,700,"Customer Name : "+str(username)+"")
    p.drawString(110,720,"Customer Address : "+str(customer.address)+"") 
    p.drawString(110,740,"Customer Phone No : "+str(customer.phone_no)+"") 
    
    p.showPage()  
    p.save()  
    return response

def home(request):
    return HttpResponse("Hello, world. You're at the main index.")
# Create your views here.
