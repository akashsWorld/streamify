import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import UserSerializer, LoginUserSerializer
from .models import User
from media.models import Channel
from rest_framework import status


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class Authenticate(APIView):
    def post(self, request: Request):
        request_data = request.data

        login_user = LoginUserSerializer(data=request_data)
        login_user.is_valid(raise_exception=True)

        user = User.objects.filter(email=request_data['email'])
        if user.exists():
            user = user.first()
            if str(user.password) == request_data['password']:
                # TODO: This is a demo purpose implementation.
                channel = Channel.objects.filter(pk=user.id)
                token = uuid.uuid4()
                user.token = token
                user.save()
                return Response(data={
                    'user_name': user.user_name,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'token': token,
                    'channel_name': channel.first().channel_name if channel.exists() else None
                }, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
