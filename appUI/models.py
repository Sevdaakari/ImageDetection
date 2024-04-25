from django.db import models


class UploadedImage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user_image = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.title

