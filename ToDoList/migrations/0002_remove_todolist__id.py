# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='_id',
        ),
    ]
