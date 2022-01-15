from django.urls import path
from .views import RegisterView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    
]
