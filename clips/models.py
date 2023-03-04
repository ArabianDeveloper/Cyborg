from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clip(models.Model):
    clipper = models.ForeignKey(User, verbose_name="clipper", on_delete=models.CASCADE, related_name='clipper')
    title = models.CharField(max_length=50)
    viewers = models.ManyToManyField(User, verbose_name="viewer", related_name='viewer', null=True, blank=True)
    v_link = models.URLField(max_length=255)

    def __str__(self):
        return self.title