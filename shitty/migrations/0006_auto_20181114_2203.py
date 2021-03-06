# Generated by Django 2.0.8 on 2018-11-14 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0005_auto_20181114_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='DislodgeDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shitty.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='dis_dates',
            field=models.ManyToManyField(blank=True, to='shitty.DislodgeDates'),
        ),
    ]
