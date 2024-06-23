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
        return channel

    def update(self, instance: Channel, validated_data: Channel):
        instance.channel_description = validated_data['channel_description']
        instance.channel_name = validated_data['channel_name']
        instance.save()
        return instance


