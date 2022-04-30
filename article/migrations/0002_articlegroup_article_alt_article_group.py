# Generated by Django 4.0.4 on 2022-04-30 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='files/images/articles')),
                ('alt', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='alt',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.articlegroup'),
            preserve_default=False,
        ),
    ]
