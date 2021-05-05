from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogView,AuthorName,Comment
from .forms import BlogViewForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth import get_user_model
User=get_user_model()
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
class HomePageView(TemplateView):
    template_name = 'landing/home.html'

class BlogPage(ListView):
    model = BlogView
    template_name = 'landing/blog.html'
    context_object_name = 'data'

def blogpage(request):
    data=BlogView.objects.all()
    print(request.POST)
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
    de=get_object_or_404(BlogView,id=id)
    b=BlogView.objects.get(id=id)
    c=Comment.objects.filter(blogview_id=id)
    print(len(c))
    print(c)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(name=form.cleaned_data['name'],
                            user=request.user,
                            blogview=b)
            comment.save()
            return redirect('/landing/blog/')
    else:
        form=CommentForm()
    return render(request,'landing/detail.html',{'de':de,'form':form,'comment':c,'total_likes':de.total_likes(),'comment_length':len(c)})

def Create(request):
    if request.method=='POST':
        form=BlogViewForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            print(form.cleaned_data['image'])
            updated = form.save(commit=False)
            updated.title = form.cleaned_data["title"]
            updated.summary = form.cleaned_data["summary"]
            updated.blogs = form.cleaned_data["blogs"]
            updated.image=form.cleaned_data['image']
            updated.user = request.user
            updated.save()
            print('Form is valid',form.cleaned_data)
            return redirect('/landing/blog/')
        else:
            print('Invalid')
    else:
        form=BlogViewForm()
    return render(request,'landing/create.html',{'form':form})

def updateblog(request,id):
    blog_object=get_object_or_404(BlogView,id=id)
    if request.method=='POST':
        form=BlogViewForm(request.POST,instance=blog_object)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form=BlogViewForm()
    return render(request,{'form':form})


class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = BlogView
    template_name = 'landing/confirm_delete.html'
    success_url = '/landing/home'

    def test_func(self):
        desc = self.get_object()
        if self.request.user == desc.user:
            return True
        return False

def blogdelete(request,blog_id):
    b=get_object_or_404(BlogView,id=blog_id)
    if request.user == b.user:
        b.delete()
    else:
        print('Cannot be deleted',request.user.id,b.user.id)
    return redirect('/landing/blog')

def BlogTry(request):
    return render(request,'landing/blogtry.html')

def like_blog(request):
    print(request.POST)

    blog=get_object_or_404(BlogView,id=request.POST.get('blog_id'))
    blog.likes.add(request.user)
    return HttpResponseRedirect(blog.get_absolute_url())

