from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    user_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "user_name",
            "bio",
            "avatar",

            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "last_logout",
            "date_joined",
        ]
        read_only_fields = [
            "id",
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
