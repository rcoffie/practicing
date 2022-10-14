from django.shortcuts import render, redirect
from todo.models import Post
from todo.forms import PostForm
# Create your views here.


def list_posts(request):
    posts = Post.objects.all()
    context = {'posts':posts,}

    return render(request, 'list_post.html',context)


def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    context = {'form':form}
    return render(request, 'create_post.html',context)

def edit_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(".")

    context = {'form':form,}
    return render(request, 'edit_post.html',context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post_detail.html',context)

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("list_posts")
