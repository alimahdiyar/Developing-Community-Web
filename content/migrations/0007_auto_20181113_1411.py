# Generated by Django 2.0.9 on 2018-11-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0006_auto_20181109_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
