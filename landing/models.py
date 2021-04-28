from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class AuthorName(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name

class BlogView(models.Model):
    title=models.CharField(max_length=100)
    summary=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    blogs=models.TextField(null=True)

    def __str__(self):
        return self.title