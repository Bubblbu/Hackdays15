# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_auto_20151124_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='paragraphs',
        ),
        migrations.AddField(
            model_name='article',
            name='specialwords',
            field=models.TextField(null=True, verbose_name=b'Spezialw\xc3\xb6rter'),
        ),
    ]
