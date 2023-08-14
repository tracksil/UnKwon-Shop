from django.contrib.auth import authenticate
from drf_util.decorators import serialize_decorator
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.serializers import RegisterUserSerializer, LoginUserSerializer


class UserAuthenticationViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    @action(detail=False, methods=["POST"], serializer_class=LoginUserSerializer)
    @serialize_decorator(LoginUserSerializer)
    def login(self, request, *args, **kwargs):
        user = authenticate(email=request.valid["email"], password=request.valid["password"])

        if user is not None:
            refresh = RefreshToken.for_user(user=user)
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(data)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
