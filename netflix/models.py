from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.CharField(max_length=50, blank=True, null=True)
    view_count = models.CharField(max_length=50, blank=True, null=True)
    poster = models.URLField(max_length=1000)
    backdrop = models.URLField(max_length=1000, blank=True, null=True)
    logo = models.URLField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=100)
    is_hero = models.BooleanField(default=False)

    def __str__(self):
        return self.title
