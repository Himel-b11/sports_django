# Generated by Django 4.0.5 on 2022-06-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('ADMIN', 'Admin'), ('PLAYER', 'Player')], default='STUDENT', max_length=100),
        ),
    ]
