from rest_framework import serializers
from django.db import DatabaseError, transaction
from .models import Channel, Video
import os
from django.core.files.storage import default_storage
import uuid

from .tasks import process_video, process_updated_video


class ChannelSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    channel_name = serializers.CharField(max_length=50, allow_blank=False)
    channel_description = serializers.CharField(max_length=1000, min_length=20, allow_blank=False)

    @transaction.atomic
    def create(self, validated_data):
        user_id = validated_data['id']
        channel = Channel(id_id=user_id
                          , channel_name=validated_data['channel_name'],
                          channel_description=validated_data['channel_description'])
        try:
            channel.save()
        except DatabaseError:
            return {
                'message': 'Failed',
                'saved_object': None
            }
        return {
            'message': 'Success',
            'saved_object': channel
        }

    @transaction.atomic
    def update(self, instance: Channel, validated_data: Channel):
        instance.channel_description = validated_data['channel_description']
        instance.channel_name = validated_data['channel_name']

        try:
            instance.save()
        except DatabaseError:
            return {
                'message': 'Failed',
                'saved_object': None
            }
        return {
            'message': 'Success',
            'saved_object': instance
        }


class VideoSerializer(serializers.Serializer):
    channel_id = serializers.UUIDField()
    video_id = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=300, allow_blank=False)
    description = serializers.CharField(max_length=1000, allow_blank=False)
    video_extension = serializers.CharField(max_length=10, required=False)
    thumbnail_extension = serializers.CharField(max_length=10, required=False)
    video = serializers.FileField(allow_empty_file=False, max_length=None, required=False, use_url=False)
    thumbnail = serializers.ImageField(allow_empty_file=False, max_length=None, required=False, use_url=False)

    # The default valid is automatically handled
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

    @transaction.atomic
    def create(self, validated_data):
        # Create the file name
        video = validated_data['video']
        thumbnail = validated_data['thumbnail']
        title = validated_data['title']

        _, image_extension = os.path.splitext(thumbnail.name)
        _, video_extension = os.path.splitext(video.name)
        video_id = uuid.uuid4()
        new_file_name = f'{video_id}-{title}'

        video.name = new_file_name
        thumbnail.name = new_file_name

        video = Video(
            title=title,
            description=validated_data['description'],
            url=new_file_name,
            thumbnail_extension=image_extension,
            genra=validated_data['genra'],
            search_string=validated_data['search_string'],
            hash_tags=validated_data['hash_tags'],
            channel_id=Channel(id_id=validated_data['channel_id'])
        )

        try:
            video.save()
        except DatabaseError:
            return {
                'message': 'Failed',
                'saved_object': None
            }

        # try:
        #     # TODO: Uncomment if the lines commented below to save the data in localstorage.
        #     # default_storage.save(f'./images/{new_file_name}{image_extension}', thumbnail)
        #     # default_storage.save(f'./temp/{new_file_name}{video_extension}', video)
        #
        # except IOError as err:
        #     # Handle the err Operation
        #     print(err)
        #     return {
        #         'message': 'Failed',
        #         'saved_object': None
        #     }

        # TODO:Enable the video processing feature.
        # process_video.delay(
        #     video_name=new_file_name,
        #     video_id=video.id,
        #     extension=video_extension
        # )
        return {
            'message': 'Success',
            'saved_object': video
        }

    @transaction.atomic
    def update(self, instance: Video, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.genra = validated_data['genra']
        instance.hash_tags = validated_data['hash_tags']
        instance.search_string = validated_data['search_string']

        is_new_video_exist = True if 'video' in validated_data else False
        is_new_thumbnail_exist = True if 'thumbnail' in validated_data else False

        if is_new_video_exist:
            instance.status = 'PEND'
        if is_new_thumbnail_exist:
            instance.thumbnail_extension = validated_data['thumbnail_extension']

        try:
            instance.save()
        except DatabaseError:
            return {
                'message': 'Failed',
                'saved_object': None
            }

        # Saving the video to temp storage and send for processing.
        try:
            if is_new_video_exist:
                video = validated_data['video']
                video_name = instance.url
                video.name = video_name
                video_extension = validated_data['video_extension']
                # TODO: Enable the saving and processing part
                # default_storage.save(f'./temp/{video_name}{video_extension}', video)
                # process_updated_video.delay(video_name, instance.id, video_extension)

            # Saving the Updated Image to localstorage and Delete the old one.
            if is_new_thumbnail_exist:
                thumbnail = validated_data['thumbnail']
                thumbnail_name = instance.url
                thumbnail.name = thumbnail_name
                file_path_str = f'./images/{thumbnail_name}{validated_data["thumbnail_extension"]}'
                # TODO: TO Enable the saving part.
                # default_storage.delete(file_path_str)
                # default_storage.save(file_path_str, thumbnail)

        except IOError:
            # Handle the Operation to reverse the Operation of saving file in storage.
            return {
                'message': 'Failed',
                'saved_object': None
            }

        return {
            'message': 'Success',
            'saved_object': instance
        }
