from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels


class ArticleGroup(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='files/images/articles')
    alt = models.CharField(max_length=64, default='alt')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(ArticleGroup, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images/articles')
    alt = models.CharField(max_length=64, default='alt')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Article, self).save(*args, **kwargs)
