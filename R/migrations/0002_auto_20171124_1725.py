# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('R', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='R.Usuarios'),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='R.Usuarios'),
        ),
    ]
