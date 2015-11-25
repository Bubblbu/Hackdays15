# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_auto_20151124_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='specialwords',
            field=models.TextField(null=True, verbose_name=b'Spezialw\xc3\xb6rter', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.TextField(null=True, verbose_name=b'Untertitel', blank=True),
        ),
    ]
