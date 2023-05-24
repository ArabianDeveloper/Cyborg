from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Stream(models.Model):
    title = models.CharField(max_length=50)
    streamer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='streams')
    game = models.OneToOneField("games.Game", on_delete=models.CASCADE, related_name='streams')
    image = models.URLField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    viewers = models.ManyToManyField(User, related_name='stream_viewer', blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title