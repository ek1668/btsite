# Generated by Django 3.0.5 on 2021-09-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baaleit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bt',
            name='age',
            field=models.CharField(default='', max_length=60),
        ),
    ]
