# Generated by Django 4.0.4 on 2022-04-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='alt',
            field=models.CharField(default='alt', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='alt',
            field=models.CharField(default='alt', max_length=32),
        ),
    ]
