
from django.shortcuts import render

from blogs.models import Blog, Category
from assignments.models import About

def home(request):
    featured_blog = Blog.objects.filter(is_featured=True,status='Published')
    blogs = Blog.objects.filter(is_featured=False, status='Published')
    about = About.objects.get()

    context =  {
        'featured_blog' : featured_blog,
        'blogs' : blogs,
        'about' : about,
    }
    return render(request , "index.html", context)