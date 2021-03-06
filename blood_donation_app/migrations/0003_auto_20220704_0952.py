# Generated by Django 3.2.13 on 2022-07-04 09:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation_app', '0002_disease_request_userdisease'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=datetime.datetime(2022, 7, 4, 9, 52, 24, 808017, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='acknowledge_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
