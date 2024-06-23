from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from user.models import User
from .constants import get_genera


class Channel(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=50)
    channel_description = models.TextField()
    created_on = models.DateField(auto_now_add=True)


class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    playlist_name = models.CharField(max_length=100)


class Video(models.Model):
    choice = (
        ('GEN', 'GENERAL'),
        ('TECH', 'TECHNOLOGY'),
        ('LEARN', 'LEARNING_TEACHING'),
        ('ENT', 'ENTERTAINMENT'),
        ('ANI', 'ANIME'),
        ('MU', 'SONGS_MUSIC'),
        ('MOV', 'MOVIES'),
        ('MED', 'MEDICAL')
    )

    id = models.UUIDField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    url = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500,null=True)
    uploaded_on = models.DateTimeField(auto_now=True)
    genera = ArrayField(models.CharField(max_length=20, choices=choice), default=get_genera)
    search_string = models.TextField(default='')
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE,default='-')
    playlist_id = models.ForeignKey(Playlist, on_delete=models.SET_NULL,null=True)


class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    comment = models.TextField(null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_comment')
    comment_on = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
