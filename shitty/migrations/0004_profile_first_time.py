# Generated by Django 2.0.8 on 2018-11-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0003_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_time',
            field=models.BooleanField(default=False),
        ),
    ]
