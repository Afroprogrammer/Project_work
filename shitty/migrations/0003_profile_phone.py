# Generated by Django 2.0.9 on 2018-11-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0002_auto_20181110_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
