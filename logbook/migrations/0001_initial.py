# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('utente', models.CharField(unique=True, max_length=50)),
                ('log', models.TextField(max_length=300)),
                ('data_apertura', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
