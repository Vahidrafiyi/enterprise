from django.db import models
from django_jalali.db import models as jmodels


class Service(models.Model):
    title_fa = models.CharField(max_length=32)
    title_en = models.CharField(max_length=32)
    body_fa = models.TextField()
    body_en = models.TextField()
    image = models.ImageField(upload_to='files/images/services')
    alt = models.CharField(max_length=32, default='alt')

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Service, self).save(*args, **kwargs)


class Project(models.Model):
    title_fa = models.CharField(max_length=32)
    title_en = models.CharField(max_length=32, null=True, blank=True)
    body_fa = models.TextField()
    body_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='files/images/projects')
    alt = models.CharField(max_length=32, default='alt')
    start_time_fa = jmodels.jDateField()
    start_time_en = jmodels.jDateField(null=True, blank=True)
    end_time_fa = jmodels.jDateField()
    end_time_en = jmodels.jDateField(null=True, blank=True)
    doing_time_fa = jmodels.jDateField()
    doing_time_en = jmodels.jDateField(null=True, blank=True)

    def __str__(self):
        return self.title_fa

    def save(self, *args, **kwargs):
        self.alt = self.title_fa
        super(Project, self).save(*args, **kwargs)
