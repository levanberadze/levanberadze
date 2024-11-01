from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', context={'posts': posts})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', context={'post': post})