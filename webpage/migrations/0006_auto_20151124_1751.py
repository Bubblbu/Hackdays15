# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20151124_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.TextField(null=True, verbose_name=b'Untertitel'),
        ),
    ]
