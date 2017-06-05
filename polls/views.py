from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from django.views.generic import ListView

from polls.models import question, choice


def index(request):
    a=question.objects.order_by('-pub_date')[:5]
    context ={'question': a}
    template = "polls/index.html"
    return render (request,template,context)

def question_result(request,id):
    a= question.objects.get(id=int(id))
    c=choice.objects.filter(question=a)
    context ={'question': a,'choices':c}
    template = "polls/result.html"
    return render (request,template,context)

#def question_details(request,id):
     #q= question.objects.get(id=int(id))
    # context ={'question': q,}
     #template = "polls/question.html"
    # return render (request,template, context)


class QuestionDetailView(generic.DetailView):
     model= question
     template_name='polls/question.html'


class QuestionListView(ListView):
     model= question
     template_name='polls/index.html'

def question_vote(request,id):
    a= question.objects.get(id=int(id))
    c=choice.objects.filter(question=a)
    context ={'question': a,'choices':c}
    template = "polls/vote.html"
    if request.method == "POST":
        print (request.POST['choice'])
        id=int(request.POST['choice'])
        c=choice.objects.get(id=id)
        c.votes+= 1
        c.save()
        return redirect("view_result", a.id)

    else:
        return render (request,template, context)


class QuestionDetailView(object):
    pass
