# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20150919_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Google Chrome', max_length=200, choices=[(b'Google Chrome', b'Google Chrome'), (b'Mozilla Firefox', b'Mozilla Firefox'), (b'Internet Explorer', b'Internet Explorer'), (b'Safari', b'Safari')])),
                ('version', models.CharField(max_length=200, blank=True)),
                ('operating_system', models.CharField(default=b'OSX', max_length=200, choices=[(b'OSX', b'OSX'), (b'Win7', b'Windows 7'), (b'Win8', b'Windows 8'), (b'Win10', b'Windows 10')])),
                ('project', models.ForeignKey(to='projects.Project', null=True)),
            ],
        ),
    ]
