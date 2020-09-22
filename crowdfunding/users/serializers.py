from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    image = serializers.URLField()
    date_created = serializers.DateTimeField()
    project_owner = serializers.BooleanField()

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


