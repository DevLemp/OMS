# Generated by Django 3.0.3 on 2020-04-21 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_movie_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_movie',
            old_name='user',
            new_name='user_id',
        ),
    ]