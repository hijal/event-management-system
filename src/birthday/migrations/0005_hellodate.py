# Generated by Django 2.2.4 on 2019-08-21 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_auto_20190821_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
