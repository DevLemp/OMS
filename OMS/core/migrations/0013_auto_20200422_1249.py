# Generated by Django 3.0.3 on 2020-04-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200422_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_movie',
            name='insert_date',
            field=models.DateTimeField(default='2020-04-22 11:49:14', editable=False),
        ),
    ]
