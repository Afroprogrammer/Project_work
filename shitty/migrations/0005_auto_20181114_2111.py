# Generated by Django 2.0.8 on 2018-11-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0004_profile_first_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_time',
            field=models.BooleanField(default=True),
        ),
    ]