from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    doesntmatter = Question.objects.all()
    return render(request,"polls/index.html",{"latest_question_list":doesntmatter})


def detail(request,question_id):
    question_is=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"value" : question_is})


def results(request,question_id):
    return HttpResponse(f'You are looking the results of Question {question_id} ' )


def vote(request,question_id):
    return HttpResponse(f'You are voting the question number {question_id} ' )