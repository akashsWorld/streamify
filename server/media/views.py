from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChannelSerializer
from .models import Channel


class ChannelView(APIView):
    def post(self, request):
        data = request.data
        exists = Channel.objects.filter(pk=data['id']).exists()
        if exists:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = ChannelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def put(self,request):
        serializer = ChannelSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
