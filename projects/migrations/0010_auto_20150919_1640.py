# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150919_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browser',
            name='operating_system',
            field=models.CharField(default=b'OSX', max_length=200, choices=[(b'OSX', b'OSX'), (b'Win7', b'Windows 7'), (b'Win8', b'Windows 8'), (b'Win10', b'Windows 10')]),
        ),
    ]
