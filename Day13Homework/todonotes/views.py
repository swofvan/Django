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

from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from .forms import Add_Notes

from .models import Notes
from .serializers import NotesSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data = request.data)

    if form.is_valid():
        user = form.save()
        return Response ('Account created successfully!', status = status.HTTP_201_CREATED)
    
    return Response (form.errors, status = status.HTTP_400_BAD_REQUEST)



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


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addnotes(request):
    form = Add_Notes(request.data)
    if form.is_valid():
        notes = form.save()
        return Response({'id': notes.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def list_note(request):
    note = Notes.objects.all()
    serializer = NotesSerializer(note, many=True)
    return Response(serializer.data)



# You are helping to build a personal to-do notes app for students. Students should be able to register,
# log in, and manage their own notes using APIs.

# Your tasks:
   
# Create a signup API so users can register using a username and password.

# Create a login API that gives a token and the username after successful login.

# Create an API to add a note (with a title and message). Only logged-in users should be able to add a note.

# Create an API to list all notes. Only logged-in users should be able to see them.

