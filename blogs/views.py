from django.shortcuts import render, get_object_or_404

from blogs.models import Category, Blog


# Create your views here.
def blog_by_category(request, category_id):
    # category = get_object_or_404(Category, pk=category_id)

    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        pass
    #category = Category.objects.get(pk=category_id)



    context = {
        'posts': Blog.objects.filter(status='Published',category=category_id).order_by('-created_at'),
        'category': category
    }
    return render(request,'blog_by_category.html', context)