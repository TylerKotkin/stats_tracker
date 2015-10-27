# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('act_title', models.CharField(max_length=100)),
                ('act_description', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
                ('date_done', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='stats_app.Activity')),
            ],
        ),
    ]
