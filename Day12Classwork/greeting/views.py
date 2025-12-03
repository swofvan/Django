from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .forms import Productform

from .models import Products
from .serializers import ProductSerializer

@api_view(['POST'])
@permission_classes((AllowAny,))

def create_product(request):
    form = Productform(request.POST)

    if form.is_valid():
        product = form.save()
        return Response ({'id' : product.id}, status = status.HTTP_201_CREATED)
    
    return Response (form.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((AllowAny,))

def list_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Create a simple  API that sends a list of products as a response. 
# Each product should have a name, price, and category. 
# The data should be created manually inside the view and returned when someone accesses the endpoint.