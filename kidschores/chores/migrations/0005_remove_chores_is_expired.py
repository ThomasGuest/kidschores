# Generated by Django 2.2.1 on 2019-06-03 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0004_chores_is_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chores',
            name='is_expired',
        ),
    ]