# Generated by Django 2.0.9 on 2018-11-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0005_auto_20181109_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(default='content', max_length=1000),
            preserve_default=False,
        ),
    ]
