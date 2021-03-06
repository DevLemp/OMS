# Generated by Django 3.0.3 on 2020-04-13 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200413_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_movie',
            name='insert_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='user_movie',
            name='status',
            field=models.CharField(default='available', editable=False, max_length=255),
        ),
    ]
