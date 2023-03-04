# Generated by Django 4.1.5 on 2023-02-09 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clips', '0003_clip_v_link_clip_viewers_alter_clip_clipper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='viewers',
            field=models.ManyToManyField(blank=True, null=True, related_name='viewer', to=settings.AUTH_USER_MODEL, verbose_name='viewer'),
        ),
    ]