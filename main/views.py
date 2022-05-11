from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth.models import User
from main.models import Customer, Product, Bill
from .serialzier import CustomerSerializer, ProductSerializer, BillSerializer
from rest_framework.response import Response

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
    new_bill = BillSerializer(data=request.data)

def home(request):
    return HttpResponse("Hello, world. You're at the main index.")
# Create your views here.
