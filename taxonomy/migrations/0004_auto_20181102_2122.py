# Generated by Django 2.0.9 on 2018-11-02 21:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('taxonomy', '0003_remove_term_title_fa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termrelation',
            old_name='source',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='termrelation',
            old_name='destination',
            new_name='term',
        ),
    ]
