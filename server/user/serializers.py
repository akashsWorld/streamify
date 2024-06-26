from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user
