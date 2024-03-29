# Generated by Django 4.1.5 on 2023-05-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0008_alter_stream_viewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='stream_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Streams/images/%d/'),
        ),
    ]
