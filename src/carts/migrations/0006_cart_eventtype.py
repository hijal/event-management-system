# Generated by Django 2.2.4 on 2019-08-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_hellodate'),
        ('carts', '0005_auto_20190825_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='eventType',
            field=models.ManyToManyField(to='birthday.EventType'),
        ),
    ]
