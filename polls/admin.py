from __future__ import unicode_literals
from polls.models import question
from polls.models import choice

from django.contrib import admin

# Register your models here.
admin.site.register(question)
admin.site.register(choice)

