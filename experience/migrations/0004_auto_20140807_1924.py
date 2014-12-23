# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_auto_20140806_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='rating_score',
            field=models.IntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='camp',
            name='rating_votes',
            field=models.PositiveIntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='experience',
            name='rating_score',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='rating_votes',
        ),
        migrations.RemoveField(
            model_name='involvement',
            name='rating',
        ),
    ]
