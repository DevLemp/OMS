# Generated by Django 3.0.3 on 2020-04-21 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200421_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_movie',
            name='duration',
        ),
        migrations.AddField(
            model_name='user_movie',
            name='insert_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]