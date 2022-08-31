# Generated by Django 4.0.5 on 2022-08-31 04:36

from django.db import migrations, models
import utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_remove_team_players_teamplayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.helpers.file_upload_directory),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.helpers.file_upload_directory),
        ),
    ]