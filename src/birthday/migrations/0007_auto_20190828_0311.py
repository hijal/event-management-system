# Generated by Django 2.2.4 on 2019-08-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0006_eventtype_dam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='dam',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
