# Generated by Django 4.0.4 on 2022-05-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0007_rename_name_menu_title_en_menu_title_fa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='address',
            new_name='address_fa',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='phone',
            new_name='phone_fa',
        ),
        migrations.RenameField(
            model_name='logo',
            old_name='logo_text',
            new_name='logo_text_fa',
        ),
        migrations.AddField(
            model_name='footer',
            name='address_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='phone_en',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_text_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
