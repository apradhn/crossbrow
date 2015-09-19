# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150919_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browser',
            name='name',
            field=models.CharField(default=b'Google Chrome', max_length=200, choices=[(b'Google Chrome', b'Google Chrome'), (b'Mozilla Firefox', b'Mozilla Firefox'), (b'Internet Explorer', b'Internet Explorer'), (b'Safari', b'Safari')]),
        ),
    ]
