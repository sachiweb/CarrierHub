from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('app',views.app,name="app"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('services/',views.services,name="services"),
    path('landing',views.landing,name="landing"),
    path('mlroad',views.mlroad,name="mlroad"),
    path('webroad',views.webroad,name="webroad"),
    path('androad',views.androad,name="androad"),
    path('add',views.add,name="add"),
    
    # path('signout',views.signout,name="signout"),
    # path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    
]