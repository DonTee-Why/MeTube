# Generated by Django 3.2.2 on 2021-06-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meTube', '0003_alter_appuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Login'),
        ),
    ]
