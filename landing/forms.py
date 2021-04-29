from django.forms import ModelForm
from .models import BlogView, Comment

class BlogViewForm(ModelForm):
    class Meta:
        model=BlogView
        fields=['title','blogs','summary','image']

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['name']

