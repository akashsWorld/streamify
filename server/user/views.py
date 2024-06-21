from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
import os


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        return Response('ok')


