from rest_framework import serializers, validators
from django.contrib.auth.hashers import make_password

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "email", "first_name", "last_name"]

        extra_kwargs = {
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        queryset=CustomUser.objects.all(),
                        message="Username already taken.",
                    )
                ],
            },
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        queryset=CustomUser.objects.all(),
                        message="An account is already registered with that email.",
                    ),
                ],
            },
        }

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        email = validated_data.get("email")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")

        user = CustomUser.objects.create(
            username=username.lower(),
            password=make_password(password),
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        return user
