# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordnet', '0004_auto_20140709_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='domain',
            field=models.ForeignKey(to='wordnet.Domain', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='definition',
            name='definition',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='definition',
            name='term',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
