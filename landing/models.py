from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    image=models.ImageField(default='default.jpg',upload_to='author_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    blogs=models.TextField(null=True)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("landing:detail", args=[self.id])

class Comment(models.Model):
    name=models.CharField(max_length=500)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blogview=models.ForeignKey(BlogView,on_delete=models.CASCADE)