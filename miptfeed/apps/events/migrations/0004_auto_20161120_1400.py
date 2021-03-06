# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=256, verbose_name='место проведения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=256, verbose_name='мероприятие'),
        ),
    ]
