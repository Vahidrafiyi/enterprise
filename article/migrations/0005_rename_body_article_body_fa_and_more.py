# Generated by Django 4.0.4 on 2022-05-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_articlegroup_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='body_fa',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='title_fa',
        ),
        migrations.RenameField(
            model_name='articlegroup',
            old_name='title',
            new_name='title_fa',
        ),
        migrations.AddField(
            model_name='article',
            name='body_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='articlegroup',
            name='title_en',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]