# Generated by Django 2.1.5 on 2019-05-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20190515_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourmoviecd',
            name='rank',
        ),
        migrations.AlterField(
            model_name='ourmoviecd',
            name='audiAcc',
            field=models.TextField(null=True),
        ),
    ]
