from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    video_url = models.CharField(max_length=2083)


