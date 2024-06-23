from django.urls import path
from .views import ChannelView, VideoView

urlpatterns = [
    path('channel/', ChannelView.as_view()),
    path('upload/', VideoView.as_view())
]
