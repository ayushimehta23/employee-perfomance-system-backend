# core/views.py
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

# HR creates users
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only superusers/HR

# List users (optional, for HR)
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
