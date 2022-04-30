from django.db import models
from django_jalali.db import models as jmodels


class News(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images/news')
    alt = models.CharField(max_length=128)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(News, self).save(*args, **kwargs)


class Slider(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='files/images/sliders')
    alt = models.CharField(max_length=128)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Slider, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='files/images/products')
    alt = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Product, self).save(*args, **kwargs)


class Comment(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images/comments')
    alt = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Comment, self).save(*args, **kwargs)


class Partner(models.Model):
    image = models.ImageField(upload_to='files/images/partner')
    alt = models.CharField(max_length=128)

    def __str__(self):
        return self.alt
