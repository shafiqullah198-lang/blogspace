from django.urls import path
from .views import index,about,login,contact,blog,blog_detail



urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('contact/', contact, name='contact'), 
    path("blog/", blog, name="blog"),
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),


]
