from django.db import models
from django.conf import settings


class Chatroom(models.Model):
    room_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Messages(models.Model):
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )
    message = models.CharField(max_length=600)
