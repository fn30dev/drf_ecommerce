# Generated by Django 4.0.5 on 2022-06-09 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='is_active',
        ),
    ]