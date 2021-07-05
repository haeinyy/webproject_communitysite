# Generated by Django 3.2.4 on 2021-07-05 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_name', models.CharField(max_length=15, verbose_name='사용자이름')),
                ('user_pw', models.CharField(max_length=15, verbose_name='비밀번호')),
                ('user_phone', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='휴대폰번호')),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'member_member',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('nickname', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
    ]
