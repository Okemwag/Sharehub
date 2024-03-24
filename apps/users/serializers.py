# Serializers for the user model:

from rest_framework import serializers
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_email_verified",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "last_logout",
            "date_joined",
        ]
        read_only_fields = [
            "id",
            "is_email_verified",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "last_logout",
            "date_joined",
        ]
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }