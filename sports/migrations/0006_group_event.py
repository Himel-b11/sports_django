# Generated by Django 4.0.5 on 2022-08-31 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_event_image_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sports.event'),
        ),
    ]
