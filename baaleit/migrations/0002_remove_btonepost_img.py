# Generated by Django 3.0.5 on 2021-10-11 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baaleit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btonepost',
            name='img',
        ),
    ]