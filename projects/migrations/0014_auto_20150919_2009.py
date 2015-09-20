# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20150919_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='browser',
            name='project',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='project',
        ),
        migrations.RemoveField(
            model_name='test',
            name='feature',
        ),
        migrations.DeleteModel(
            name='Browser',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
