# core/urls.py
from django.urls import path
from .views import CustomAuthToken, CreateUserView, ListUsersView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/', ListUsersView.as_view(), name='list_users'),
]
