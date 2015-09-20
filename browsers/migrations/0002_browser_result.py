# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='browser',
            name='result',
            field=models.CharField(blank=True, max_length=200, choices=[((b'Pass',), b'Pass'), (b'Fail', b'Fail')]),
        ),
    ]
