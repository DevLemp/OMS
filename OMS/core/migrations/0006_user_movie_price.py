# Generated by Django 3.0.3 on 2020-04-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200414_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_movie',
            name='price',
            field=models.FloatField(default=1),
        ),
    ]
