# Generated by Django 2.1.1 on 2018-11-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181120_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='openflights_id',
            field=models.IntegerField(null=True),
        ),
    ]
