from django.db import models
from django_jalali.db import models as jmodels


class Service(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images/services')
    alt = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Service, self).save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images/projects')
    alt = models.CharField(max_length=32)
    start_time = jmodels.jDateField()
    end_time = jmodels.jDateField()
    doing_time = jmodels.jDateField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.alt = self.title
        super(Project, self).save(*args, **kwargs)
