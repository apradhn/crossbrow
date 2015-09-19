# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150919_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
