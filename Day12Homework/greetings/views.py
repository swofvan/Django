from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes((AllowAny,))

def signup(request):
    form = UserCreationForm(data = request.data)

    if form.is_valid():
        user = form.save()
        return Response ('Account created successfully!', status = status.HTTP_201_CREATED)
    
    return Response (form.errors, status = status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))

def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response ({'error':'Please provide both username and password'}, 
                         status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid User'},
                        status=HTTP_404_NOT_FOUND)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)

# Create two APIs:
# One for creating a new account using a name and password.
# Another for logging into an account. After successful login, it should return the user's name and a secret key (token).