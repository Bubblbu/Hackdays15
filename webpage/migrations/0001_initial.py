# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titel')),
                ('body', models.TextField(verbose_name=b'Inhalt')),
                ('date_created', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ressort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='ressort',
            field=models.ForeignKey(to='webpage.Ressort'),
        ),
    ]
