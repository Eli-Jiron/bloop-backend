from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from utils.authentication import CookieJWTAuthentication

from .models import Users
from .serializers import RegisterUserSerializer, UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(Users, email=request.data["email"])
        if not user.check_password(request.data["password"]):
            return Response(
                {"detail": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST
            )

        token = RefreshToken.for_user(user)
        response = Response(status=status.HTTP_200_OK)
        response.set_cookie(key="access_token", value=token.access_token, httponly=True)
        response.set_cookie(key="refresh_token", value=token, httponly=True)
        return response


class LoginRefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = RefreshToken(refresh_token)
            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(key="access_token", value=token.access_token, httponly=True)
            return response
        except TokenError:
            return Response(
                {"detail": "Token is invalid or expired"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


class MyProfileView(RetrieveAPIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
