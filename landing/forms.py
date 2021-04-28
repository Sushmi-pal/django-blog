from django.forms import ModelForm
from .models import BlogView

class BlogViewForm(ModelForm):
    class Meta:
        model=BlogView
        fields=['title','blogs','summary','image']

