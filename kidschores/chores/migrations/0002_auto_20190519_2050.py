# Generated by Django 2.2.1 on 2019-05-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
