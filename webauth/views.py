from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from hackathon import settings
from django.core.mail import send_mail
from .models import Post


def home(request):
    if request.method == 'POST':
        # auth=Authpage(request.POST)
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request,"user already exists")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"email already exists")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"user name must be under 10 charecter")
            return redirect('home')
        if len(password)<6:
            messages.error(request,"password can be more then 6 digits")
            return redirect('home')
 
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('app') 
    
    return render(request,"index.html")

def app(request):
    return render(request,"app.html")

def about(request):
    return render(request,"about.html")

# def teacher(request):
#     return render(request,"teacher.html")
def services(request):
    return render(request,"solanding.html")
def landing(request):
    return render(request,"landing.html")
def mlroad(request):
    return render(request,"ML_road.html")
def webroad(request):
    return render(request,"web_road.html")
def androad(request):
    return render(request,"android_road.html")


def blog(request):
    featured_post = Post.objects.all().filter(category=0)[:1]
    django_post = Post.objects.all().filter(fram=0)[:2]
    flask_post = Post.objects.all().filter(fram=1)[:2]

    context = {'featured_post':featured_post,'django_post':django_post,'flask_post':flask_post}
    
    return render(request, 'blog.html', context)


def add(request):
    if request.method == 'POST':
        title=request.POST['title']
        category=request.POST['category']
        fram=request.POST['fram']
        thumbnail=request.POST['thumbnail']
        body=request.POST['body']
        summary=request.POST['summary']

        post=Post(title=title,category=category,fram=fram,thumbnail=thumbnail,body=body,summary=summary)
        post.save()
        return redirect('blog')
    # else:
    #     return redirect('add')
    return render(request, 'add_blog.html')



def signin(request):
    if request.method == 'POST':
        user_name=request.POST['uname']
        user_pass=request.POST['password']
        user=authenticate(username=user_name,password=user_pass)
        print(user_name)
        if user is not None:
            login(request,user)
            messages.success(request,'congrates')
            return redirect('app')
            
        else:
            messages.error(request,'bad request')
            return redirect('signin')
    return render(request,"sign_in.html")


# def signout(request):
#     logout(request)
#     messages.success(request, "log out successfully")
#     return render(request, 'signin.html')
