# Generated by Django 2.2.3 on 2019-08-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20190818_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='Latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='Longitude',
            field=models.FloatField(null=True),
        ),
    ]
