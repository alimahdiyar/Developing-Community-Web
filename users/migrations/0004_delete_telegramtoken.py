# Generated by Django 2.0.7 on 2018-09-30 16:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20180930_1619'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TelegramToken',
        ),
    ]
