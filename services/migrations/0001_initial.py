# Generated by Django 4.0.4 on 2022-04-30 08:11

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='files/images/projects')),
                ('alt', models.CharField(max_length=32)),
                ('start_time', django_jalali.db.models.jDateField()),
                ('end_time', django_jalali.db.models.jDateField()),
                ('doing_time', django_jalali.db.models.jDateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='files/images/services')),
                ('alt', models.CharField(max_length=32)),
            ],
        ),
    ]
