# Generated by Django 2.2.4 on 2019-08-23 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birthday', '0005_hellodate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday.HelloDate')),
                ('eventtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday.EventType')),
                ('forwhom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday.ForWhom')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday.Guest')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
