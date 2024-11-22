from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer
from rest_framework.views import APIView
from rest_framework import viewsets


# Create your views here.

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