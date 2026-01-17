# admin_auth/urls.py
from django.urls import path
from .views import*
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path("profile/", AdminProfileView.as_view()),
    path("change-password/", AdminPasswordChangeView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),
]
