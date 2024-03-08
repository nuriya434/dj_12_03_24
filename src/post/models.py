from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    # str fields:
    mobile_phone = models.CharField(max_length=12)
    # date fields:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # related fields:
    user = models.OneToOneField(to=User, related_name='account', on_delete=models.CASCADE)
    # under methods:
    def __str__(self) -> str:
        return f'{self.id} --- {self.mobile_phone}'
    
    class Meta:
        db_table = 'UserAccount'
        ordering = ('-created_at',)
        verbose_name = 'User account'
        verbose_name_plural = 'User accounts'

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} --- {self.title}'
    
    class Meta:
        db_table = 'Category'
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Post-Categories'

class Post(models.Model):
    # str fields:
    title = models.CharField(max_length=255)
    # bool fields:
    is_active = models.BooleanField(default=False)
    # date fields:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # related fields:
    user = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        to=Category,
        related_name='posts',
    )

    # dunder methods:
    def __str__(self) -> str:
        return f'{self.id} --- {self.title}'
    
    class Meta:
        db_table = 'Post'
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
