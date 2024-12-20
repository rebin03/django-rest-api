from django.urls import path
from api import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('token/', views.ObtainAuthToken.as_view()),
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/<int:pk>/', views.PostRetriveUpdateDestroyView.as_view()),
]
