# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 15:21
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_auto_20170227_2219'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='link',
            managers=[
                ('with_votes', django.db.models.manager.Manager()),
            ],
        ),
    ]
