# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breadtimesite', '0003_auto_20160809_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(height_field='url_height', upload_to='static/img/upload', width_field='url_width'),
        ),
    ]
