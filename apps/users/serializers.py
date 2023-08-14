from drf_util.serializers import BaseModelSerializer
from rest_framework import serializers

from apps.users.models import User


class RegisterUserSerializer(BaseModelSerializer):
    repeat_password = serializers.CharField(write_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = User
        read_only_fields = (
            *BaseModelSerializer.Meta.read_only_fields,
            "last_login",
            "blocked",
            "is_active",
            "email_verified",
            "is_superuser",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
        )

    def save(self, **kwargs):
        repeat_password = self.validated_data.pop("repeat_password")

        if repeat_password == self.validated_data.get("password"):
            user = super().save(**kwargs)
            user.set_password(self.validated_data.get("password"))
            user.save()
            return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
