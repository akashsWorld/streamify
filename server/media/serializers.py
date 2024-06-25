from rest_framework import serializers
from .models import Channel, Video
from .tasks import process_video


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


class VideoSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    title = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=1000)
    url = serializers.CharField(max_length=500)
    video_id = serializers.UUIDField()
    genra = serializers.ListField(
        child=serializers.CharField(
            max_length=10
        )
    )
    hash_tags = serializers.ListField(
        child=serializers.CharField(
            max_length=50
        )
    )
    search_string = serializers.CharField(max_length=500)

    def create(self, validated_data):
        video = Video(
            title=validated_data['title'],
            description=validated_data['description'],
            url=validated_data['url'],
            thumbnail=validated_data['url'],
            genra=validated_data['genra'],
            search_string=validated_data['search_string'],
            hash_tags=validated_data['hash_tags'],
            channel_id=validated_data['user_id']
        )
        saved_video = video.save()
        process_video.delay()
        return {}

