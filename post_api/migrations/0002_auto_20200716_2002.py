# Generated by Django 3.0.8 on 2020-07-16 17:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleuser',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_liked',
            field=models.DateField(default=datetime.datetime(2020, 7, 16, 17, 2, 32, 941589, tzinfo=utc)),
        ),
    ]
