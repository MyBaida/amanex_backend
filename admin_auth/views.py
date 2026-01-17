# admin_auth/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_staff:
            return Response(
                {"error": "Not authorized as admin"},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "admin": {
                "id": user.id,
                "email": user.email,
                "name": user.get_full_name(),
            }
        })


class AdminProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("USER: ", request.user)
        print('AUTH: ', request.auth)
        user = request.user

        if not user.is_staff:
            return Response({"error": "Unauthorized"}, status=403)

        return Response({
            "username": user.username,
            "email": user.email
        })

    def put(self, request):
        user = request.user

        if not user.is_staff:
            return Response({"error": "Unauthorized"}, status=403)

        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.save()

        return Response({"message": "Profile updated successfully"})


class AdminPasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        if not user.is_staff:
            return Response({"error": "Unauthorized"}, status=403)

        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")

        if not user.check_password(current_password):
            return Response(
                {"error": "Current password is incorrect"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validate_password(new_password, user)
        except ValidationError as e:
            return Response({"error": e.messages}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password changed successfully"})
