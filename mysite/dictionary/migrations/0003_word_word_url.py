# Generated by Django 3.1.6 on 2021-02-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20210215_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='word_url',
            field=models.SlugField(default=123),
            preserve_default=False,
        ),
    ]
