# Generated by Django 2.0.8 on 2018-11-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shitty', '0010_tippingpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipalities',
            name='tipping_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shitty.TippingPoints'),
        ),
    ]
