# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats_app', '0002_auto_20151027_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(default=1, related_name='questions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
