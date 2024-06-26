from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    def post(self, request):
        # TODO: need to create a JWT token
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved_user = serializer.save()
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
