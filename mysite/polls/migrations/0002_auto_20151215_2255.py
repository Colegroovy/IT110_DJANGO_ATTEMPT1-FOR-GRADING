# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_textj',
            new_name='choice_text',
        ),
    ]
