# Generated by Django 2.2.4 on 2019-08-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20190822_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
