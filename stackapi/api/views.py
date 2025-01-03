from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication, permissions
from api.serializers import AnswerSerializer, UserSerializer, QuestionSerializer
from api.models import Question
from api.permissions import IsOwnerOnly, IsOwnerOrReadOnly

# Create your views here.

class SignUpView(CreateAPIView):
    
    serializer_class = UserSerializer
    

class QuestionCreateListView(CreateAPIView, ListAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    
    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)
        
        
        
class QuestionRetriveUpdateDestroyView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    
    
# QuestionAnswerView
# AnswerUpvoteDownvoteView
# ProfileUpdateView

class QuestionAnswerView(CreateAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOnly]
    
    serializer_class = AnswerSerializer
    
    