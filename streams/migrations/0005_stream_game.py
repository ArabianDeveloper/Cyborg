# Generated by Django 4.1.5 on 2023-02-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_game_downloaders'),
        ('streams', '0004_alter_stream_viewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='game',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stream', to='games.game'),
            preserve_default=False,
        ),
    ]
