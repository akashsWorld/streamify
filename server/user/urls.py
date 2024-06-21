from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.as_view()),
    path('authenticate/', UserView.as_view())
]
