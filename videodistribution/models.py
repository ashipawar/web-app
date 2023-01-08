from django.db import models

# Create your models here.

#This model has three fields:
# a title field to store the title of the video, 
# a description field to store a description of the video,
# and a video_file field to store the actual video file.

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('sci-fi', 'Sci-Fi'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField() 
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='videos/thumbnails/',default='')
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES,default='action')
