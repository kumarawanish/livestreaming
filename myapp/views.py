from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, StreamSerializer
from .models import Stream

class CreateUser(generics.CreateAPIView):
    """
    View to create a new user.
    Uses the UserSerializer to validate and save the user data.
    Allows any user (even unauthenticated) to access this endpoint.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomObtainAuthToken(ObtainAuthToken):
    """
    View to obtain an authentication token.
    Overrides the post method to include the user ID and email in the response.
    Allows any user (even unauthenticated) to access this endpoint.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'email': token.user.email})

class LiveStreamCreate(generics.CreateAPIView):
    """
    View to create a new live stream event.
    Uses the StreamSerializer to validate and save the stream data.
    Requires the user to be authenticated.
    """
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LiveStreamList(generics.ListAPIView):
    """
    View to list all active live stream events.
    Uses the StreamSerializer to serialize the stream data.
    Allows any user (even unauthenticated) to access this endpoint.
    """
    queryset = Stream.objects.filter(is_active=True)
    serializer_class = StreamSerializer
    permission_classes = [AllowAny]


class LiveStreamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a live stream event.
    Uses the StreamSerializer to serialize the stream data.
    Requires the user to be authenticated.
    """
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated]
