# Generated by Django 2.0.5 on 2018-07-23 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180720_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.AddField(
            model_name='teacher',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
