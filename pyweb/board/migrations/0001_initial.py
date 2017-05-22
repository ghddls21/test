# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('제목', models.CharField(max_length=200)),
                ('내용', models.TextField(null=True, blank=True)),
                ('조회수', models.IntegerField()),
                ('작성자', models.CharField(max_length=50)),
                ('등록일', models.DateTimeField()),
                ('수정일', models.DateTimeField()),
            ],
        ),
    ]
