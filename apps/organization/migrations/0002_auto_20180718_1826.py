# Generated by Django 2.0.5 on 2018-07-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='work_years',
            field=models.IntegerField(default=0, verbose_name='工作年限'),
        ),
    ]
