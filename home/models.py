from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class PDF(models.Model):
    title = models.CharField(max_length=255)
    image = ResizedImageField(size=[576, 256], crop=['top','left','right'], upload_to='images/books')
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    pdf = CloudinaryField(resource_type="auto")
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "PDF's"

    def get_absolute_url(self):
        return reverse('home')