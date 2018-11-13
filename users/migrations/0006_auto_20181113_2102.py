# Generated by Django 2.0.9 on 2018-11-13 21:02

import sorl.thumbnail.fields
from django.db import migrations

import users.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_profile_telegram_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True,
                                                   upload_to=users.models.profile_image_upload_location),
        ),
    ]
