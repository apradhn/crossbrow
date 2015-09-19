# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150919_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browser',
            name='version',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
