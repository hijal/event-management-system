# Generated by Django 2.2.4 on 2019-08-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0006_eventtype_dam'),
        ('carts', '0007_auto_20190827_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date',
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.ManyToManyField(to='birthday.HelloDate'),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='forwhom',
        ),
        migrations.AddField(
            model_name='cart',
            name='forwhom',
            field=models.ManyToManyField(to='birthday.ForWhom'),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='guest',
        ),
        migrations.AddField(
            model_name='cart',
            name='guest',
            field=models.ManyToManyField(to='birthday.Guest'),
        ),
    ]
