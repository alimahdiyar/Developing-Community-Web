# Generated by Django 2.0.6 on 2018-07-18 09:56

from django.db import migrations, models
import django.db.models.deletion
import taxonomy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_fa', models.CharField(max_length=255)),
                ('taxonomy_type', models.CharField(choices=[(taxonomy.models.TaxonomyType('learning_field'), 'learning_field'), (taxonomy.models.TaxonomyType('subject'), 'subject')], default=taxonomy.models.TaxonomyType('subject'), max_length=30)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Term')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]