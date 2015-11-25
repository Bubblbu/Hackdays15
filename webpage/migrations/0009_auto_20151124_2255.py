# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20151124_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='paragraphs',
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=0, verbose_name=b'Inhalt', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='raw_body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
