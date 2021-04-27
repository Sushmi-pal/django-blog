from django.contrib import admin
from .models import BlogView,AuthorName
# Register your models here.

admin.site.register(BlogView)
admin.site.register(AuthorName)