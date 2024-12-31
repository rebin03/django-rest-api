from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from api.serializers import CommentSerializer, ProfileSerializer, UserSerializer, PostSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions, authentication
from api.models import Post, Profile
from api.permissions import IsOwnerOnly, IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


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
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        
        context['request'] = self.request
        
        return context
        
        
class PostRetriveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    
class PostLikeView(APIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        post_obj = Post.objects.get(id=id)
        
        liked = False
        
        if request.user in post_obj.liked_by.all():
            post_obj.liked_by.remove(request.user)
        else:
            post_obj.liked_by.add(request.user)
            liked = True
        
        return Response(data={'message':'Ok', 'Liked':liked})
    
    
class PostCommentView(CreateAPIView):
    
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        
        id = kwargs.get('pk')
        post_object = Post.objects.get(id=id)
        
        if serializer.is_valid():
            
            serializer.save(post=post_object, owner=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
class ProfileUpdateView(UpdateAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(owner=self.request.user)
