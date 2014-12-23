# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordnet', '0005_auto_20140710_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='domain',
            field=models.ForeignKey(blank=True, to='wordnet.Domain', null=True),
        ),
        migrations.AlterField(
            model_name='definition',
            name='instance_of',
            field=models.ManyToManyField(to=b'wordnet.Definition', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='definition',
            name='lexical_id',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
