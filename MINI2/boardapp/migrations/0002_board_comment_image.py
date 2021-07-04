# Generated by Django 3.2.4 on 2021-07-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boardapp.boardallcontentlist')),
            ],
        ),
        migrations.CreateModel(
            name='Board_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField(null=True)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='boardapp.boardallcontentlist')),
            ],
        ),
    ]