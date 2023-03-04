# Generated by Django 4.1.5 on 2023-02-09 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('streams', '0003_stream_streamer_stream_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='viewers',
            field=models.ManyToManyField(blank=True, null=True, related_name='stream_viewer', to=settings.AUTH_USER_MODEL),
        ),
    ]