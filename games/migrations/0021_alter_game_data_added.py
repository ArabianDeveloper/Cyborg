# Generated by Django 4.1.5 on 2023-02-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_alter_game_data_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='data_added',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
