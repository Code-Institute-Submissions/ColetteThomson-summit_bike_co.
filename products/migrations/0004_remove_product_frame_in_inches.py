# Generated by Django 3.2 on 2022-05-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220518_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='frame_in_inches',
        ),
    ]
