# Generated by Django 3.0.3 on 2020-04-13 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_user_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_movie',
            name='insert_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user_movie',
            name='status',
            field=models.BinaryField(default=1),
        ),
    ]
