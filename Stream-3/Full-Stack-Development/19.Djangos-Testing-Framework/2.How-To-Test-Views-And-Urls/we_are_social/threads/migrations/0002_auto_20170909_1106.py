# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='Subject',
            new_name='subject',
        ),
    ]