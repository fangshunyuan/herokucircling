# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('time', models.DateTimeField(verbose_name=b'time of activity')),
                ('location', models.CharField(max_length=200)),
                ('max_pax', models.IntegerField(max_length=5)),
                ('cost', models.IntegerField(max_length=5)),
                ('curr_pax', models.IntegerField(max_length=5)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
