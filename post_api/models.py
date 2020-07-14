from time import time

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    """Model for posts at site"""

    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    content = models.TextField(blank=True)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    @staticmethod
    def generate_slug(title):
        """generate new slug for new title"""
        new_slug = slugify(title, allow_unicode=True)
        return new_slug + '_' + str(int(time()))

    def save(self, *args, **kwargs):
        """save new generated slug"""
        if not self.id:
            self.slug = self.generate_slug(self.title)
        super().save(*args, **kwargs)
