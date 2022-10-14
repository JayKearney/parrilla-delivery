# Generated by Django 3.2.15 on 2022-09-23 18:16

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0002_auto_20220923_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'),
        ),
    ]
