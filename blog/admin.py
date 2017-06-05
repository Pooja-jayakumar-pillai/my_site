from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from blog.models import post, comment
admin.site.register(post)
admin.site.register(comment)
