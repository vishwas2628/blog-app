from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect

from blog_main.forms import RegisterForm
from blogs.models import Blog, Category
from assignments.models import About
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    context = {
        "form" : form,
    }
    return render(request , "register.html" , context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')