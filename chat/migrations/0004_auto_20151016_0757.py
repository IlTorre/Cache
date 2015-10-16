# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_messaggio_immagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messaggio',
            name='messaggio',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='messaggio',
            name='risposta',
            field=models.TextField(max_length=1000),
        ),
    ]
