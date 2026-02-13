
from django.shortcuts import render

from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_blog = Blog.objects.filter(is_featured=True,status='Published')
    blogs = Blog.objects.filter(is_featured=False, status='Published')

    context =  {
        'categories' : categories,
        'featured_blog' : featured_blog,
        'blogs' : blogs,
    }
    return render(request , "index.html", context)