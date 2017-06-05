from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    user=models.ForeignKey(User)
    title=models.CharField(max_length=512)
    content=models.TextField()
    img=models.ImageField(upload_to='blog_img/')
    date=models.DateTimeField(auto_now=True,auto_now_add=False)
    is_published=models.BooleanField(default=False)


class comment(models.Model):
        user=models.ForeignKey(User)
        post=models.ForeignKey(post)
        comment_text=models.CharField(max_length=500)
        date=models.DateTimeField(auto_now=True,auto_now_add=False)
