from django.db import models
from django_jalali.db import models as jmodels


class News(models.Model):
    title_fa = models.CharField(max_length=64)
    title_en = models.CharField(max_length=64, null=True, blank=True)
    body_fa = models.TextField()
    body_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='files/images/news')
    alt = models.CharField(max_length=64, default='alt')
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(News, self).save(*args, **kwargs)


class Slider(models.Model):
    title_fa = models.CharField(max_length=128)
    title_en = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='files/images/sliders')
    alt = models.CharField(max_length=128, default='alt')
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Slider, self).save(*args, **kwargs)


class Product(models.Model):
    title_fa = models.CharField(max_length=128)
    title_en = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='files/images/products')
    alt = models.CharField(max_length=128, default='alt')

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Product, self).save(*args, **kwargs)


class Comment(models.Model):
    title_fa = models.CharField(max_length=128)
    title_en = models.CharField(max_length=128, null=True, blank=True)
    body_fa = models.TextField()
    body_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='files/images/comments')
    alt = models.CharField(max_length=128, default='alt')

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Comment, self).save(*args, **kwargs)


class Partner(models.Model):
    image = models.ImageField(upload_to='files/images/partner')
    alt = models.CharField(max_length=128, default='alt')

    def __str__(self):
        return self.alt


class Visit(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    date = jmodels.jDateField()

    def __str__(self):
        return str(self.date)
