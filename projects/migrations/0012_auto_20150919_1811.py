# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_feature_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='actual_result',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='expected_result',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
