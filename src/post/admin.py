# admin.py
from django.contrib import admin
from .models import Post
from . import models
admin.site.register(Post)

# @admin.register(models.Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_at', 'updated_at', 'is_active']
#     readonly_fields=[
#         'created_at',
#         'updated_at,'
#     ]
