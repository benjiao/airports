# Generated by Django 2.1.1 on 2018-11-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181120_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='iata',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='icao',
            field=models.CharField(max_length=4, null=True),
        ),
    ]