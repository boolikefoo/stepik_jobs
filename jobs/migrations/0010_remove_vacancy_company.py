# Generated by Django 3.0.5 on 2020-04-18 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20200418_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
    ]
