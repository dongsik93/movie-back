# Generated by Django 2.2.2 on 2019-07-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20190516_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='video',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourmoviedetail',
            name='video',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='Participating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='actors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='actors_img',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='actors_role',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='dialog',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='genres',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='image_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='large_image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='nationNm',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='openDt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='rating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='score_reple_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='score_reple_like',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='score_reples',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='showTm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='story',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ourmoviedetail',
            name='watchGradeNm',
            field=models.CharField(max_length=100, null=True),
        ),
    ]