# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.CharField(max_length=200)),
                ('definition', models.TextField()),
                ('lexical_id', models.CharField(max_length=300, null=True)),
                ('instance_of', models.ManyToManyField(to='wordnet.Definition', null=True)),
                ('parent_of', models.ManyToManyField(to='wordnet.Definition', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
