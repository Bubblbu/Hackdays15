# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressort',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
