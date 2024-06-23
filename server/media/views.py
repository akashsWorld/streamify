from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChannelSerializer
from .models import Channel
from server.settings import MEDIA_URL,MEDIA_ROOT
from django.core.files.storage import default_storage
import uuid
import os

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
        file = request.FILES['video']
        channel_id = request.POST.get('channel_id')

        # print(file.name)
        # print(channel_id)
        name, extension = os.path.splitext(file.name)
        # print(_)

        new_file_name = f'{uuid.uuid4()}-{name}{extension}'
        default_storage.save(new_file_name,file)
        # print(MEDIA_ROOT)

        return Response('empty Object', status=status.HTTP_201_CREATED)
