from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    user_name = models.CharField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
