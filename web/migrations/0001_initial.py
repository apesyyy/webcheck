# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bussiness_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor_web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(verbose_name='监控域名')),
                ('want_code', models.IntegerField(verbose_name='期待返回值')),
                ('ret_code', models.IntegerField(blank=True, null=True, verbose_name='获得的返回值')),
                ('keyword', models.CharField(max_length=100, verbose_name='期望关键字')),
                ('ret_keyword', models.CharField(blank=True, max_length=100, null=True, verbose_name='获得的返回值')),
                ('choice_method', models.CharField(choices=[('get', 'get'), ('post', 'post')], default='get', max_length=20)),
                ('para', models.CharField(blank=True, max_length=200, null=True, verbose_name='参数')),
                ('timer', models.IntegerField(default=0, verbose_name='上次打开时间')),
                ('curr_timer', models.IntegerField(default=0, verbose_name='检测时间')),
                ('bussiness_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Bussiness_line')),
            ],
            options={
                'verbose_name': '监控网站表',
                'verbose_name_plural': '监控网站表',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('bussiness_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Bussiness_line')),
            ],
        ),
    ]