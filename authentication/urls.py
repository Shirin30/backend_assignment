from django.urls import path
from .views import RegisterAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    
]
