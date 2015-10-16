# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messaggio_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaggio',
            name='immagine',
            field=models.BooleanField(default=False),
        ),
    ]
