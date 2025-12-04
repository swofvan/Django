from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import ProductForm
from rest_framework.permissions import AllowAny

from .models import Products
from .serializers import ProductSerializer

from django.shortcuts import get_object_or_404


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_product(request):
    form = ProductForm(request.POST)

    if form.is_valid():
        product = form.save()
        return Response({'id' : product.id}, status = status.HTTP_200_OK)
    return Response(form.errors, status = status. HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_product(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((AllowAny,))
def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    form = ProductForm(request.data, instance=product)

    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response (form.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response ("Product deleted successfully")


# You are helping a shop keeper track of its products.
# Your task is to create the following features using Django backend API:
# Add a new product.
#  You must send two details for each product:
# name: the name of the product (like “Soap”)
# price: the price of the product (like 30)
# Show all the products.
# Update a product using its ID.
#    You must again send the name and price for update.
# Delete a product using its ID.