# Generated by Django 3.0.3 on 2020-04-22 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200422_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_movie',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
