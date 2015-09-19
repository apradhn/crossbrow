# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_browser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='browser',
            name='test',
        ),
        migrations.AddField(
            model_name='browser',
            name='project',
            field=models.ForeignKey(to='projects.Project', null=True),
        ),
    ]
