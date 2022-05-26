from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
	blogs = Blog.objects
	return render(request, 'home.html', {'blogs': blogs})

def new(request):
	return render(request, 'new.html')

def create(request):
	blog = Blog()
	blog.title = request.GET['title']
	blog.body = request.GET['body']
	blog.pub_date = timezone.datetime.now()
	blog.save()
	return redirect(f'/blog/{blog.id}')

def detail(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	return render(request, 'detail.html', {'blog': blog})

def delete(request, blog_id):
	Blog.objects.get(id=blog_id).delete()
	return redirect('/')

def edit(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	return render(request, 'edit.html', {'blog': blog})

def update(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	blog.title = request.POST.get('title')
	blog.body = request.POST.get('body')
	blog.pub_date = timezone.datetime.now()
	blog.save()
	return redirect(f'/blog/{blog.id}')