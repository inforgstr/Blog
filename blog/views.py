from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Category
from blog import util


def home(request):
    
    q = request.GET.get("q")
    if q:
        res = []
        for item in util.list_post():
            if q.lower()==item.lower():
                post = get_object_or_404(Post, title=item)
                return render(request, "blog/detail.html", {
                    "post": post,
                    "categories": Category.objects.all(),
                })
            if q.lower() in item.lower():
                res.append(Post.objects.filter(title=item))
            
        return render(request, "blog/search.html", {
            "categories": Category.objects.all(),
            "posts": res,
        })

    return render(request, "blog/home.html", {
        "categories": Category.objects.all(),
        "posts": Post.objects.all().order_by("-published_date")
    })


def blog(request):
    q = request.GET.get("q")
    if q:
        res = []
        for item in util.list_post():
            if q.lower()==item.lower():
                post = get_object_or_404(Post, title=item)
                return render(request, "blog/detail.html", {
                    "post": post,
                    "categories": Category.objects.all(),
                })
            if q.lower() in item.lower():
                res.append(Post.objects.filter(title=item))
            
        return render(request, "blog/search.html", {
            "categories": Category.objects.all(),
            "posts": res,
        })



    categories = Category.objects.all()
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/index.html", {
        "posts": posts,
        "categories": categories,
    })


def blog_detail(request, pk):
    q = request.GET.get("q")
    if q:
        res = []
        for item in util.list_post():
            if q.lower()==item.lower():
                post = get_object_or_404(Post, title=item)
                return render(request, "blog/detail.html", {
                    "post": post,
                    "categories": Category.objects.all(),
                })
            if q.lower() in item.lower():
                res.append(Post.objects.filter(title=item))
            
        return render(request, "blog/search.html", {
            "categories": Category.objects.all(),
            "posts": res,
        })

    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {
        "post": post,
        "categories": Category.objects.all(),
    })


def get_category(request, pk):
    q = request.GET.get("q")
    if q:
        res = []
        for item in util.list_post():
            if q.lower()==item.lower():
                post = get_object_or_404(Post, title=item)
                return render(request, "blog/detail.html", {
                    "post": post,
                    "categories": Category.objects.all(),
                })
            if q.lower() in item.lower():
                res.append(Post.objects.filter(title=item))
            
        return render(request, "blog/search.html", {
            "categories": Category.objects.all(),
            "posts": res,
        })
    

    category = get_object_or_404(Category, pk=pk)
    return render(request, "blog/get_category.html", {
        "categories": Category.objects.all(),
        "category": category,
    })
