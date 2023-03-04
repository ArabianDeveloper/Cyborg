# Generated by Django 4.1.5 on 2023-02-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_alter_game_data_added'),
        ('accounts', '0004_alter_profile_clips_alter_profile_games_downloaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='games_downloaded',
            field=models.ManyToManyField(blank=True, null=True, related_name='downloader', to='games.game', verbose_name='games_downloaded'),
        ),
    ]