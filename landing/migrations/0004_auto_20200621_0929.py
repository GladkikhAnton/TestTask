# Generated by Django 3.0.7 on 2020-06-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20200621_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileimage',
            name='height',
            field=models.PositiveSmallIntegerField(default=128),
        ),
        migrations.AlterField(
            model_name='fileimage',
            name='width',
            field=models.PositiveSmallIntegerField(default=128),
        ),
    ]
