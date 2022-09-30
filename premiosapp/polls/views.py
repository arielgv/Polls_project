from django.shortcuts import render
from django.http import HttpResponse

#from polls.models import Question, Choice

def index(request):
    return HttpResponse("This is the main page.")


def detail(request,question):
    return HttpResponse(f'Your primary key is {question} ' )


def results(request,question):
    return HttpResponse(f'You are looking the results of Question {question} ' )


def vote(request,question):
    return HttpResponse(f'You are voting the question number {question} ' )