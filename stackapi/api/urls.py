from django.urls import path
from api import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('token/', views.ObtainAuthToken.as_view()),
    path('questions/', views.QuestionCreateListView.as_view()),
    path('questions/<int:pk>/', views.QuestionRetriveUpdateDestroyView.as_view()),
    path('answer/', views.QuestionAnswerView.as_view()),
]
