from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from streams.models import Stream
from clips.models import Clip
from games.models import Game
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField(max_length = 90, blank=True, null=True)
    image = models.URLField(max_length = 255, blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.user.username
    
