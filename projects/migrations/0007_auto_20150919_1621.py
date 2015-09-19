# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150919_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browser',
            name='name',
            field=models.CharField(default=(b'C',), max_length=200, choices=[((b'C',), b'Google Chrome'), ((b'FF',), b'Mozilla Firefox'), (b'IE', b'Internet Explorer'), (b'S', b'Safari')]),
        ),
    ]
