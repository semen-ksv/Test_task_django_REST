from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Like, SimpleUser

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(SimpleUser, UserAdmin)
