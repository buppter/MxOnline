# Generated by Django 2.0.5 on 2018-07-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20180724_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='课程须知'),
        ),
    ]
