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
                ('author', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titel')),
                ('subtitle', models.TextField(null=True, verbose_name=b'Untertitel', blank=True)),
                ('specialwords', models.TextField(null=True, verbose_name=b'Spezialw\xc3\xb6rter', blank=True)),
                ('raw_body', models.TextField()),
                ('body', models.TextField(verbose_name=b'Inhalt', editable=False)),
                ('created', models.DateTimeField(editable=False)),
                ('slug', models.SlugField(max_length=80, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
                ('parent', models.ForeignKey(default=None, blank=True, to='webpage.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
                ('articles', models.ManyToManyField(to='webpage.Article', blank=True)),
                ('category', models.ForeignKey(default=None, to='webpage.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ressort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, to='webpage.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='ressort',
            field=models.ForeignKey(to='webpage.Ressort'),
        ),
    ]
