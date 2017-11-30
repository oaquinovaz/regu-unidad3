# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.TextField()),
                ('id_comentario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='R.Comentarios')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='respuestas',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='R.Usuarios'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='R.Usuarios'),
        ),
    ]