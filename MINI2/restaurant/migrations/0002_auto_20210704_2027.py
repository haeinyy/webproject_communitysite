# Generated by Django 3.2.4 on 2021-07-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rest',
            name='rest_img',
        ),
        migrations.AddField(
            model_name='rest',
            name='rest_img1',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='rest',
            name='rest_img2',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='rest',
            name='rest_img3',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='rest',
            name='rest_img4',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
