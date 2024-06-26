from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChannelSerializer, VideoSerializer
from .models import Channel, Video
from django.core.files.storage import default_storage
import uuid
import os
from utils import video_service
from .tasks import process_video
import time
from server.settings import MEDIA_ROOT


class ChannelView(APIView):
    def post(self, request, _id):
        request_data = request.data
        request_data['id'] = _id
        serializer = ChannelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        data = request.data
        exists = Channel.objects.filter(pk=data['id']).exists()
        if exists:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def put(self, request, _id):
        data = request.data
        data['id'] = _id
        serializer = ChannelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = Channel.objects.filter(pk=data['id'])
        if not instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.update(instance=instance.first(), validated_data=data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


def is_valid_video(request):
    return False if 'video' in request.FILES and request.FILES['video'].content_type.startswith('video') else True


def get_form_data(request, key):
    return request.POST.get(key)


class VideoView(APIView):

    def post(self, request, _id):
        # Here the _id is the primary_key of Channel model.
        exists = Channel.objects.filter(pk=_id).exists()

        if not exists:
            return Response('Invalid Channel id', status=status.HTTP_404_NOT_FOUND)

        # Manually handle the video validity
        if is_valid_video(request):
            return Response('Invalid media', status=status.HTTP_400_BAD_REQUEST)

        if 'thumbnail' not in request.FILES:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)

        request_data = {
            'channel_id': _id,
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'genra': list(request.POST.getlist('genra')),
            'hash_tags': list(request.POST.getlist('hash_tags')),
            'search_string': 'Big Search Field',
            'video': request.FILES['video'],
            # This thumbnail is verified by the serializer if self.
            'thumbnail': request.FILES['thumbnail']
        }

        serializer = VideoSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        saved_data = serializer.save()
        if saved_data['saved_object'] is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({'message': 'Created',
                         'video_id': saved_data['saved_object'].id},
                        status=status.HTTP_201_CREATED)

    def put(self, request, _id):
        # Here the _id is the primary_key of Video model.
        query_set = Video.objects.filter(pk=_id)

        if not query_set.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        video_obj: Video = query_set.first()

        request_data = {
            'video_id': _id,
            'channel_id': video_obj.channel_id_id,
            'title': get_form_data(request, key='title') if 'title'
                                                            in request.POST else video_obj.title,
            'description': get_form_data(request, key='description') if 'description'
                                                                        in request.POST else video_obj.description,
            'genra': request.POST.getlist('genra') if 'genra'
                                                      in request.POST else video_obj.genra,
            'hash_tags': request.POST.getlist('hash_tags') if 'hash_tags'
                                                              in request.POST else video_obj.hash_tags,
            'search_string': 'Big search String'
        }

        # TODO: if any search string dependent variable changed then update the search string

        # if False:
        #     request_data['search_string'] = video_service.create_search_string(
        #         request_data['title'],
        #         request_data['genra'],
        #         request_data['hash_tags'],
        #     )

        if not is_valid_video(request):
            video = request.FILES['video']
            _, video_extension = os.path.splitext(video.name)
            request_data['video'] = video
            request_data['video_extension'] = video_extension
        if 'thumbnail' in request.FILES:
            thumbnail = request.FILES['thumbnail']
            _, thumbnail_extension = os.path.splitext(thumbnail.name)
            request_data['thumbnail'] = request.FILES['thumbnail']
            request_data['thumbnail_extension'] = thumbnail_extension

        serializer = VideoSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        saved_data = serializer.update(instance=video_obj, validated_data=serializer.validated_data)
        if saved_data['saved_object'] is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_201_CREATED)
