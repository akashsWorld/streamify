from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def greet(request):
    return Response({'name': 'Akash Biswas'})


urlpatterns = [
    path('', greet),
]
