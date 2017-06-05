from __future__ import unicode_literals
from django.shortcuts import render

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
