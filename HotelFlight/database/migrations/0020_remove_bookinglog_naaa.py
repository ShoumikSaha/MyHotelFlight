# Generated by Django 2.2.2 on 2019-09-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_bookinglog_naaa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinglog',
            name='naaa',
        ),
    ]