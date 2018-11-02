# Generated by Django 2.0.9 on 2018-11-02 21:22

import content.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0004_auto_20181102_2122'),
        ('content', '0003_auto_20181023_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTermRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', enumfields.fields.EnumField(enum=content.models.ContentTermRelationType, max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='content',
            name='terms',
        ),
        migrations.AlterField(
            model_name='content',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contenttermrelation',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.Content'),
        ),
        migrations.AddField(
            model_name='contenttermrelation',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='taxonomy.Term'),
        ),
    ]
