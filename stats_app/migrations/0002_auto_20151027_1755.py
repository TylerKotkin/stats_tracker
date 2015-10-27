# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='activity',
            field=models.ForeignKey(related_name='stats', to='stats_app.Activity'),
        ),
    ]
