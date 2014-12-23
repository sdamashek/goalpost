# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_auto_20140804_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='latitude',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='camp',
            name='longitude',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
