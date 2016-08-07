# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(default=datetime.datetime(2016, 8, 7, 7, 19, 45, 44954, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='ocupacion',
            field=models.CharField(default=datetime.datetime(2016, 8, 7, 7, 20, 2, 153087, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='tlf',
            field=models.CharField(default=datetime.datetime(2016, 8, 7, 7, 20, 9, 849961, tzinfo=utc), max_length=11),
            preserve_default=False,
        ),
    ]
