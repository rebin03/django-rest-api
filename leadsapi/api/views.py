from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Lead
from api.serializers import LeadSerializer
from django.db.models import Count
from rest_framework import permissions, authentication

# Create your views here.

class LeadListCreateView(APIView):
    
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        
        qs = Lead.objects.all()
        # serialization
        serializer = LeadSerializer(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        # de serialization
        serializer = LeadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
class LeadRetrieveUpdateDestroyView(APIView):
    
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = LeadSerializer
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        qs = Lead.objects.get(id=id)
        serializer = self.serializer_class(qs)

        return Response(data=serializer.data)
    
    
    def delete(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        Lead.objects.get(id=id).delete()
        
        return Response(data={'message':'lead has been deleted'})
    
    
    def put(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        lead_object = Lead.objects.get(id=id)
        serializer = self.serializer_class(data=request.data, instance=lead_object)

        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
class LeadSummayView(APIView):
    
    
    def get(self, request, *args, **kwargs):
        
        total_lead_count = Lead.objects.all().count()
        
        source_summary = Lead.objects.all().values('source').annotate(count=Count('source'))
        course_summary = Lead.objects.all().values('course').annotate(count=Count('course'))
        status_summary = Lead.objects.all().values('status').annotate(count=Count('status'))
        
        context = {
            'total_lead': total_lead_count,
            'source_summary': source_summary,
            'course_summary': course_summary,
            'status_summary': status_summary,
        }
        
        return Response(data=context)