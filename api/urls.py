from django.urls import include, path
from home.views import LoginAPI, index, person, PersonView, PersonViewSet, RegisterAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index'),
    path('function/person/', person, name='person-function'),
    path('class/person/', PersonView.as_view(), name='person-class'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='signin'),
]
