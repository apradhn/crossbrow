# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
        ('test_cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('result', models.CharField(blank=True, max_length=10, choices=[(b'P', b'Pass'), (b'F', b'Fail')])),
                ('feature', models.ForeignKey(to='features.Feature')),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='feature',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
