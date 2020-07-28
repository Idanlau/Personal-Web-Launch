from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from django.contrib.auth.models import User


# Create your models here.

class Uploads(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    time =  models.DateTimeField(default=timezone.now)
    preview_img = models.ImageField(default = 'default.png', upload_to="preview_photo/")


class PostImages(models.Model):
    post = models.ForeignKey(Uploads, null = True, on_delete = models.CASCADE)
    post_imgs = models.ImageField(default='default.png', upload_to="post_photo/")

