from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length=20)
    image = ProcessedImageField(
        blank=True,
        upload_to='%Y/%m/%d',
        processors=[ResizeToFill(600, 800)],
        format='JPEG',
        options={'quality': 60},
        )