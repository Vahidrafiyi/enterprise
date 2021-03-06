# Generated by Django 4.0.4 on 2022-04-30 08:11

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='files/images/comments')),
                ('alt', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='files/images/news')),
                ('alt', models.CharField(max_length=128)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='files/images/partner')),
                ('alt', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='files/images/products')),
                ('alt', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='files/images/sliders')),
                ('alt', models.CharField(max_length=128)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
    ]
