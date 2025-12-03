from django.shortcuts import render
from datetime import date
from .models import Post, Author


# Create your views here.
def Home(request):
    latest_postes = Post.objects.all().order_by("-date")[:3]    
    return render(request, "blog/index.html", {
        "posts": latest_postes
    })


def Posts(request):

    return render(request, "blog/all-posts.html", {
        "all_posts": Post.objects.all()
   })

def PostDetail(request, id):
    identified_post = Post.objects.get(pk=id)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    }) 