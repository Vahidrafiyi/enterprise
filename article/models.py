from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels


class ArticleGroup(models.Model):
    title_fa = models.CharField(max_length=64)
    title_en = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to='files/images/articles-group')
    alt = models.CharField(max_length=64, default='alt')

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(ArticleGroup, self).save(*args, **kwargs)


class Article(models.Model):
    title_fa = models.CharField(max_length=64)
    title_en = models.CharField(max_length=64, null=True, blank=True)
    body_fa = models.TextField()
    body_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='files/images/articles')
    alt = models.CharField(max_length=64, default='alt')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Article, self).save(*args, **kwargs)
