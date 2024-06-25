from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChannelSerializer, VideoSerializer
from .models import Channel
from django.core.files.storage import default_storage
import uuid
import os
from utils import video_service


class ChannelView(APIView):
    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = request.data
        exists = Channel.objects.filter(pk=data['id']).exists()
        if exists:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        serializer = ChannelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = Channel.objects.filter(pk=data['id'])
        if not instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.update(instance=instance.first(), validated_data=data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class VideoView(APIView):
    def post(self, request):
        user_id = request.POST.get('user_id')
        exists = Channel.objects.filter(pk=user_id).exists()

        if not exists:
            return Response('Invalid User', status=status.HTTP_404_NOT_FOUND)

        video = request.FILES['video']
        thumbnail = request.FILES['thumbnail']
        title = request.POST.get('title')

        _, image_extension = os.path.splitext(thumbnail.name)
        _, video_extension = os.path.splitext(video.name)
        video_id = uuid.uuid4()
        new_file_name = f'{video_id}-{title}'

        video.name = new_file_name
        thumbnail.name = new_file_name

        # default_storage.save(f'./images/{new_file_name}{image_extension}', thumbnail)
        # default_storage.save(f'./temp/{new_file_name}{video_extension}', video)

        request_data = {
            'user_id': user_id,
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'video_url': new_file_name,
            'genra': request.POST.get('genra'),
            'hash_tags': request.POST.get('hash_tags'),
            'video_id': video_id,
            'search_string': ''
        }

        request_data['search_string'] = video_service.create_search_string(
            request_data['title'],
            request_data['description'],
            request_data['genra']
        )
        serializer = VideoSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data,
                        status=status.HTTP_201_CREATED)
