# Generated by Django 2.1.1 on 2018-11-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20181122_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='degree',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='evcent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='pagerank',
            field=models.FloatField(null=True),
        ),
    ]
