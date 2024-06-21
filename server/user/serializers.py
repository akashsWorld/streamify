from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'password']
