from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from user.models import User
from .constants import get_genera


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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    description = models.TextField()
    url = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    genera = ArrayField(models.CharField(max_length=20, choices=choice), default=get_genera)
    search_string = models.TextField(default='')


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_comment')
    comment_on = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
