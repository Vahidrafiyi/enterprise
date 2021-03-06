# Generated by Django 3.2.8 on 2022-05-08 09:37

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0009_useractivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=0)),
                ('date', django_jalali.db.models.jDateField()),
            ],
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='last_activity',
            field=django_jalali.db.models.jDateTimeField(),
        ),
    ]
