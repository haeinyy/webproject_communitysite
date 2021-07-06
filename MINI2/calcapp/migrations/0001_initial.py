# Generated by Django 3.2.4 on 2021-07-06 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='notice_img')),
            ],
        ),
        migrations.CreateModel(
            name='Attendences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attend', models.IntegerField(default=0)),
                ('absent', models.IntegerField(default=0)),
                ('time', models.FloatField()),
                ('time_rate', models.FloatField()),
                ('day_rate', models.FloatField()),
                ('time_cum_rate', models.FloatField()),
                ('day_cum_rate', models.FloatField()),
                ('user_phone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
