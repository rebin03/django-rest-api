from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import LoginSerializer, PersonSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.

class RegisterAPI(APIView):
    
    def get(self, request, *args, **kwargs):
        
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        _data = request.data
        serializer = RegisterSerializer(data=_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Created'}, status=status.HTTP_201_CREATED)
        
        return Response({'message': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
    
    
class LoginAPI(APIView):
    
    def post(self, request, *args, **kwargs):
        
        _data = request.data
        serializer = LoginSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
        user_obj = authenticate(request, username=serializer.data.get('username'), password=serializer.data.get('password'))

        if not user_obj:
            return Response({'message':'Invalid credential'}, status=status.HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user_obj)
        
        print(_)

        return Response({'message':'Login Successfull', 'token':str(token)}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    
    if request.method == 'GET':
        people_detail = {
            "name": "Muhammed Rebin",
            "Age": 23,
            "Place": "Kozhikode"
        }
        
        return Response(people_detail)
    
    if request.method == 'POST':
        return Response("This is a POST method")
    
    if request.method == 'PUT':
        return Response("This is a PUT method")
    
    
# Implementing using class based view
class PersonView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        person_objects = Person.objects.all()
        serializer = PersonSerializer(person_objects, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request, *args, **kwargs):
        
        data = request.data
        id = data.get('id')
        
        person_obj = Person.objects.get(id=id)
        serializer = PersonSerializer(person_obj, data=data, partial=False)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request, *args, **kwargs):
        
        data = request.data
        id = data.get('id')
        
        person_obj = Person.objects.get(id=id)
        serializer = PersonSerializer(person_obj, data=data, partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request, *args, **kwargs):
        
        data = request.data
        id = data.get('id')
        
        Person.objects.get(id=id).delete()
        
        return Response({'message': 'Person deleted'})


# Implementing using function based view
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])   
def person(request):
    
    if request.method == 'GET':
        
        person_objects = Person.objects.all()
        serializer = PersonSerializer(person_objects, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        
        data = request.data
        id = data.get('id')
        
        person_obj = Person.objects.get(id=id)
        serializer = PersonSerializer(person_obj, data=data, partial=False)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)        
    
    elif request.method == 'PATCH':
        
        data = request.data
        id = data.get('id')
        
        person_obj = Person.objects.get(id=id)
        serializer = PersonSerializer(person_obj, data=data, partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        
        data = request.data
        id = data.get('id')
        
        Person.objects.get(id=id).delete()
        
        return Response({'message': 'Person deleted'})



class PersonViewSet(viewsets.ModelViewSet):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
    def list(self, request):
        
        search = request.GET.get('search')
        qs = self.queryset
        
        if search:
            
            qs = Person.objects.filter(name__startswith=search)

        serializer = PersonSerializer(qs, many=True)
        return Response({'status':200, 'data': serializer.data})