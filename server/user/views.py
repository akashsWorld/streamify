from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # This raise exception defines that if user Data is not validated then return 404.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
