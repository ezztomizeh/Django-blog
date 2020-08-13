from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
def HomePage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'home.html',context)

def UserPost(request,username):
    user = User.objects.filter(username=username).first()
    posts = Post.objects.filter(author=user).all()

    return render(request,'UserPost.html',context = {'posts' : posts})

def ViewPost(request,pk):
    post = Post.objects.get(pk = pk)
    context = {
        'post' : post
    }
    return render(request,'Post.html',context)

@login_required
def CreatePost(requset):
    if requset.method == 'POST':
        title = requset.POST['title']
        content = requset.POST['content']
        author = User.objects.filter(username=requset.user).first()
        post = Post(title=title,content=content,author=author)
        post.save()
        messages.success(requset,f'{title}, Has been posted')
        return redirect('blog-home')
    else:
        return render(requset,'CreatePost.html')

@login_required
def UpdatePost(request,pk):
    author = Post.objects.get(pk = pk).author
    if request.user == author:
        if request.method == 'POST':
            post = Post.objects.get(pk = pk)
            title = request.POST['title']
            content = request.POST['content']
            post.title = title
            post.content = content
            post.save()
            messages.success(request,'Post Updated')
            return redirect('ViewPost',pk=pk)
        else:
            post = Post.objects.get(pk = pk)
            return render(request,'UpdatePost.html',context={'post':post})
    else:
        messages.error(request,'You are not the author')
        return redirect('ViewPost',pk=pk)

@login_required
def DeletePost(request,pk):
    author = Post.objects.get(pk = pk).author
    if request.user == author:
        post = Post.objects.get(pk = pk)
        post.delete()
        return redirect('blog-home')
    else:
        messages.error(request,'You are not the author')
        return redirect('ViewPost' , pk = pk)