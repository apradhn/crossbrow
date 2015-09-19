# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20150919_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='actual_result',
        ),
        migrations.RemoveField(
            model_name='test',
            name='expected_result',
        ),
        migrations.AddField(
            model_name='test',
            name='result',
            field=models.CharField(blank=True, max_length=10, choices=[(b'P', b'Pass'), (b'F', b'Fail')]),
        ),
    ]
