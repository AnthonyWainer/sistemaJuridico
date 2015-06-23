# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.BooleanField(default=True)),
                ('idexpedientes', models.ForeignKey(to='expediente.expedientes')),
                ('idpermisos', models.ForeignKey(to='seguridad.permisos')),
            ],
        ),
    ]
