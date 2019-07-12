# Generated by Django 2.2.3 on 2019-07-12 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('audience', models.IntegerField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieCd', models.TextField()),
                ('rank', models.TextField()),
                ('audiAcc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieNm', models.CharField(max_length=100)),
                ('showTm', models.IntegerField()),
                ('openDt', models.DateField()),
                ('nationNm', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=100)),
                ('actors_img', models.CharField(max_length=100)),
                ('actors_role', models.CharField(max_length=100)),
                ('watchGradeNm', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('large_image', models.CharField(max_length=200)),
                ('story', models.TextField()),
                ('rating', models.CharField(max_length=100)),
                ('Participating', models.CharField(max_length=100)),
                ('score_reples', models.TextField()),
                ('score_reple_id', models.TextField()),
                ('score_reple_like', models.TextField()),
                ('dialog', models.CharField(max_length=100)),
                ('movieCd', models.TextField()),
                ('rank', models.TextField()),
                ('audiAcc', models.TextField()),
                ('show1', models.CharField(max_length=100)),
                ('show2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OurMovieCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieCd', models.TextField()),
                ('audiAcc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='OurMovieDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieNm', models.CharField(max_length=100)),
                ('showTm', models.IntegerField()),
                ('openDt', models.DateField()),
                ('nationNm', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=100)),
                ('actors_img', models.CharField(max_length=100)),
                ('actors_role', models.CharField(max_length=100)),
                ('watchGradeNm', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('large_image', models.CharField(max_length=200)),
                ('story', models.TextField()),
                ('rating', models.CharField(max_length=100)),
                ('Participating', models.CharField(max_length=100)),
                ('score_reples', models.TextField()),
                ('score_reple_id', models.TextField()),
                ('score_reple_like', models.TextField()),
                ('dialog', models.CharField(max_length=100)),
                ('movieCd', models.TextField()),
                ('audiAcc', models.TextField()),
                ('show1', models.CharField(max_length=100)),
                ('show2', models.CharField(max_length=100)),
                ('average', models.FloatField(null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='like_post_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
