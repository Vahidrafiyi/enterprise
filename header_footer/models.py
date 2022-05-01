from django.db import models


class SocialMedia(models.Model):
    image = models.ImageField(upload_to='files/images/social-media')
    alt = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social media'


class Footer(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)


class Menu(models.Model):
    title_fa = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_en


class Logo(models.Model):
    logo_text = models.CharField(max_length=120)
    logo_alt = models.TextField(default='')
    logo_image = models.ImageField(upload_to='files/images/logo', null=True, blank=True)

    def __str__(self):
        return self.logo_text

    def save(self, *args, **kwargs):
        self.logo_alt = self.logo_text
        super(Logo, 'self').save(*args, **kwargs)  # Call the "real" save() method.
