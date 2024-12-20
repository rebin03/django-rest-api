from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Property
from api.serializers import PropertySerializer
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.

class PropertyCreateListView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        qs = Property.objects.all()
        serializer = PropertySerializer(qs, many=True)
        
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
class PropertyRetrieveUpdateDestroyView(APIView):
    
    serializer_class = PropertySerializer
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        property_object = Property.objects.get(id=id)
        serializer = self.serializer_class(property_object)
        
        return Response(data=serializer.data)
    
    
    def put(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        property_object = Property.objects.get(id=id)
        serializer = self.serializer_class(data=request.data, instance=property_object)

        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
    def delete(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        Property.objects.get(id=id).delete()
        
        return Response(data={'message': 'Property has been deleted succesfully!'})
    
    
class PropertySummary(APIView):
    
    def get(self, request, *args, **kwargs):
        
        total_property = Property.objects.all().count()
        
        qs = Property.objects.all()
        category_summary = qs.values('category').annotate(count=Count('category'))
        bedroom_count_summary = qs.values('bedroom_count').annotate(count=Count('bedroom_count'))
        
        context = {
            'total_count': total_property,
            'category_summary': category_summary,
            'bedroom_summary': bedroom_count_summary,
        }
        
        return Response(data=context)