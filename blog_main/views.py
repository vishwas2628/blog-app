
from django.shortcuts import render

from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_blog = Blog.objects.filter(is_featured=True)
    print(featured_blog)

    context =  {
        'categories' : categories,
        'featured_blog' : featured_blog,
    }
    return render(request , "index.html", context)