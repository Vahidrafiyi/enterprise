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


class Header(models.Model):
    parent = models.CharField(max_length=16)
    child = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.parent
