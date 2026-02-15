
from django.shortcuts import render

from blogs.models import Blog, Category

def home(request):
    featured_blog = Blog.objects.filter(is_featured=True,status='Published')
    blogs = Blog.objects.filter(is_featured=False, status='Published')

    context =  {
        'featured_blog' : featured_blog,
        'blogs' : blogs,
    }
    return render(request , "index.html", context)