from django.urls import path
from api import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('token/', views.ObtainAuthToken.as_view()),
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/<int:pk>/', views.PostRetriveUpdateDestroyView.as_view()),
    path('posts/<int:pk>/add-like/', views.PostLikeView.as_view()),
    path('posts/<int:pk>/add-comment/', views.PostCommentView.as_view()),
    path('profile/change/', views.ProfileUpdateView.as_view()),
]
