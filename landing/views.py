from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogView,AuthorName
from .forms import BlogViewForm
from django.contrib.auth import get_user_model
User=get_user_model()
from django.views.generic import ListView, DetailView
class HomePageView(TemplateView):
    template_name = 'landing/home.html'

class BlogPage(ListView):
    model = BlogView
    template_name = 'landing/blog.html'
    context_object_name = 'data'

def blogpage(request):
    data=BlogView.objects.all()
    return render(request,'landing/blogcreate.html',{'data':data})

def authdesc(request,user_id):
    print('hello',user_id)
    print(request.user.id)
    desc=User.objects.get(id=request.user.id)
    # desc=User.get_object_or_404(AuthorName,id=author_id)
    return render(request,'landing/authdescription.html',{'desc':desc})

class BlogDetail(DetailView):
    model = BlogView
    template_name = 'landing/detail.html'

def detailblog(request,id):
    print(id)
    # de=BlogView.objects.get(id=id)
    de=get_object_or_404(BlogView,id=id)
    return render(request,'landing/detail.html',{'de':de})

def Create(request):
    if request.method=='POST':
        form=BlogViewForm(request.POST)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.title = form.cleaned_data["title"]
            updated.summary = form.cleaned_data["summary"]
            updated.blogs = form.cleaned_data["blogs"]
            updated.user = request.user
            updated.save()
            print('Form is valid',form.cleaned_data)
            return redirect('/landing/blog/')
        else:
            print('Invalid')
    else:
        form=BlogViewForm()
    return render(request,'landing/create.html',{'form':form})

def BlogTry(request):
    return render(request,'landing/blogtry.html')
