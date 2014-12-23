# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('description', models.TextField()),
                ('url', models.URLField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('resource_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='experience.Resource')),
            ],
            options={
            },
            bases=('experience.resource',),
        ),
        migrations.AddField(
            model_name='experience',
            name='rating_score',
            field=models.IntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='rating_votes',
            field=models.PositiveIntegerField(default=0, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='experience',
            name='rating',
        ),
    ]
