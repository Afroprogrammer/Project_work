# Generated by Django 2.0.9 on 2018-11-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0015_auto_20181117_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='first_time',
            field=models.BooleanField(default=True),
        ),
    ]
