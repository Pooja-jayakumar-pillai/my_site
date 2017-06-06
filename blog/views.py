from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from blog.models import post, comment


def home(request):
    template_name ='blog/home.html'
    posts = post.objects.all()
    for i in posts:
        i.content = i.content[0:100]+"...."
    context={'object_list':posts}
    return render(request, template_name, context)


def view_post (request,id):
    posts= post.objects.get(id=int(id))
    comments = comment.objects.filter(post=posts)
    print(comments)
    template='blog/view.html'
    context= {"post":posts,"comments":comments}
    return render(request,template,context)


def add_post(request):
    if request.method =="POST":
        title=request.POST['title']
        content=request.POST['content']
        img = request.FILES['img']
        is_published = request.POST['is_published']
        user= User.objects.get(username=request.user.username)
        new_post = post(title=title, user= user, content=content,img=img,is_published=is_published)
        new_post.save()
        return redirect('post',new_post.id)
    else:
        template_name ='blog/add_post.html'
        context ={}
        return render(request,template_name,context)


def  edit_post(request,pk):
    Post= post.objects.get(id=int(pk))
    #if request.user.username!=post.user.username:
        # permission denied
     #   raise PermissionDenied
    if request.method =="GET":
        template_name ='blog/post_edit.html'
        context={'post':Post}
        return render(request,template_name,context)
    else:
        Post.title=request.POST['title']
        Post.content=request.POST['content']
        if 'img' in request.FILES:
            post.img = request.FILES["img"]
        if 'is_published' in request.POST['is_published']:
            post.is_published = request.POST['is_published']
        Post.save()
        return redirect('post',Post.id)

def delete_post(request,id):
    if post.objects.get(id=int(id)) is not None:
        p=post.objects.get(id=int(id))
        if p.user.username == request.user.username:
            p.delete()
            return redirect('home')
    raise PermissionDenied


