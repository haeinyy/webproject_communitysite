# Generated by Django 3.2.4 on 2021-07-05 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=100)),
                ('rest_score', models.FloatField(default=0)),
                ('rest_address', models.TextField(default='')),
                ('rest_kind', models.CharField(default='', max_length=100)),
                ('rest_seenum', models.IntegerField(default=1)),
                ('rest_img1', models.CharField(max_length=200)),
                ('rest_img2', models.CharField(max_length=200)),
                ('rest_url', models.URLField()),
                ('rest_rmd', models.CharField(default='user', max_length=100)),
                ('rest_update', models.DateTimeField()),
                ('rest_tel', models.CharField(default=None, max_length=15)),
                ('rest_price', models.CharField(default=None, max_length=100)),
                ('rest_starscore', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_user', models.CharField(max_length=100)),
                ('review_score', models.FloatField()),
                ('review_content', models.TextField()),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.rest')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_user', models.CharField(max_length=100)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.rest')),
            ],
        ),
    ]
