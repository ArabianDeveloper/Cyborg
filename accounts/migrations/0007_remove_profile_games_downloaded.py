# Generated by Django 4.1.5 on 2023-02-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='games_downloaded',
        ),
    ]