from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Category, Blog
from django.db.models import Q



# Create your views here.
def blog_by_category(request, category_id):

    # Use try/except when you want to need custom error handling
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except Category.DoesNotExist:
    #     # redirect to home page if category not exist
    #     return redirect('home')

    # Use get_object_or_404 when you want to show 404 error page if the category not exists
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': Blog.objects.filter(status='Published',category=category_id).order_by('-created_at'),
        'category': category,
        'title': category.category_name,
    }
    return render(request,'blog_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }

    return render(request,'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    search_blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'search_blogs': search_blogs,
    }
    return render(request, 'search.html',context)