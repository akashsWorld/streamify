from django.urls import path
from .views import ChannelView, VideoView

urlpatterns = [
    path('channel/<_id>', ChannelView.as_view()),
    path('upload/<_id>', VideoView.as_view()),
]
