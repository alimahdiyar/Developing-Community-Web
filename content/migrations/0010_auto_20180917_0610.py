# Generated by Django 2.0.7 on 2018-09-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20180917_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='content',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
