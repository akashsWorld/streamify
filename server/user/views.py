from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    def post(self, request):
        # TODO: need to create a JWT token
        print(request.data)
        # serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # saved_user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
