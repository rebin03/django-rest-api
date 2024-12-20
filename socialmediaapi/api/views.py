from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from api.serializers import UserSerializer, PostSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions, authentication
from api.models import Post
from api.permissions import IsOwnerOnly, IsOwnerOrReadOnly


# Create your views here.


class SignUpView(CreateAPIView):
    
    serializer_class = UserSerializer
    

class PostCreateListView(CreateAPIView, ListAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class PostRetriveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()