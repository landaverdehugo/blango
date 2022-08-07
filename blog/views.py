from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() 
    #server is behind 5 hours, cannot filter by timezone
    return render(request, "blog/index.html", {"posts": posts})