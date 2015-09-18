# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activities',
            name='curr_pax',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activities',
            name='max_pax',
            field=models.IntegerField(default=0),
        ),
    ]
