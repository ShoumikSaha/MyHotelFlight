# Generated by Django 2.2.3 on 2019-07-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20190730_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ifCancelled',
            field=models.BooleanField(default='False'),
        ),
    ]
