# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_ressort_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=80, editable=False),
        ),
        migrations.AlterField(
            model_name='ressort',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
