# Generated by Django 3.2 on 2021-04-18 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_user_telefono'),
        ('habitacional', '0004_auto_20210413_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.user'),
        ),
    ]