# Generated by Django 4.1.5 on 2023-02-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_game_mimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='company',
            field=models.CharField(default='sandbox', max_length=50),
            preserve_default=False,
        ),
    ]