from rest_framework import serializers
from .models import Channel
from user.models import User
from user.serializers import UserSerializer


class ChannelSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    channel_name = serializers.CharField(max_length=50, allow_blank=False)
    channel_description = serializers.CharField(max_length=1000, min_length=20, allow_blank=False)

    def create(self, validated_data):

        user_id = validated_data['id']
        channel = Channel(id_id=user_id
                          , channel_name=validated_data['channel_name'],
                          channel_description=validated_data['channel_description'])
        channel.save()
        print(channel)
        return {}

    def update(self, instance, validated_data):
        print('Running Update method')
        print(instance)
        print(validated_data)
        return instance
