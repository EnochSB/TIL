from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        upload_to='%Y/%m/%d',
        processors=[ResizeToFit(1080, 720)],
        format='JPEG',
        options={'quality': 60},
        )
    movie = models.CharField(max_length=50)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)