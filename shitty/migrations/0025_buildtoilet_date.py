# Generated by Django 2.0.9 on 2018-11-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0024_buildtoilet'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildtoilet',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
