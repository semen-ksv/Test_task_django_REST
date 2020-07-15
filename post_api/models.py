from time import time

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Like(models.Model):
    """Model of like what user leave for post"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    date_liked = models.DateField(default=timezone.now())


class SimpleUser(models.Model):
    """Model of User with additional fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    biography = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    last_login = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    """Model for posts at site"""

    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    content = models.TextField(blank=True)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = GenericRelation(Like)

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

    @property
    def total_likes(self):
        return self.likes.count()


