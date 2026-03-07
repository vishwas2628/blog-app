from django.shortcuts import render, redirect,get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blog_count': blog_count
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()

    context= {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    # Simpler way of editing a category
    # form = CategoryForm(instance=Category.objects.get(id=pk)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    all_post = Blog.objects.all()

    context = {
        'all_post': all_post
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temp save the form data
            post.author = request.user # add the current user as author
            post.save() # ave post first so we use it id for add in slug field
            title = form.cleaned_data.get('title')
            # slugify the title and add the id to it so if any case the tittle is same it make different the slug.
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print("form is not valid")
            print(form.errors)
    form = BlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            print("form is not valid")
            print(form.errors)
    form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html',context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')
