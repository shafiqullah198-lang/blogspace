from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    q = request.GET.get("q", "")
    posts = Post.objects.filter(is_published=True).order_by("-created_at")

    if q:
        posts = posts.filter(title__icontains=q)

    return render(request, "blog.html", {"posts": posts, "q": q})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, "blog_detail.html", {"post": post})
def about(request):
    message = "welcome to blog page"
    name = "shafiq"
    father_name = "m saeed"

    context = {
        "message": message,
        "name": name,
        "father_name": father_name,
    }

    return render(request, "about.html", context)

    
