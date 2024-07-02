from django.urls import path
from .views import CreateUser,CustomObtainAuthToken

from .views import LiveStreamCreate, LiveStreamList, LiveStreamDetail


urlpatterns = [
    path('register/', CreateUser.as_view()),
    path('token/', CustomObtainAuthToken.as_view()),
    path('streams/', LiveStreamList.as_view()),
    path('streams/create/', LiveStreamCreate.as_view()),
    path('streams/<int:pk>/', LiveStreamDetail.as_view()),
]
