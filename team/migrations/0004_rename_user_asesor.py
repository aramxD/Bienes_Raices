# Generated by Django 3.2 on 2021-04-22 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitacional', '0006_auto_20210420_1341'),
        ('team', '0003_citas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Asesor',
        ),
    ]
