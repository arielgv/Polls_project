from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question , Choice
from django.utils import timezone
 
 #CLASED BASED VIEWS
from django.views import generic
#con esto se instancia las vistas basadas en calses

class IndexView(generic.ListView):
    #template_name: "polls/index.html"
    #context_object_name: "latest_question_list"
    

    def get_queryset(self):
        #Return the last five publications
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]

class DetailView(generic.DetailView):
    model = Question
    # template_name: "polls/detail.html"

    def get_queryset(self):
        # Excluye any future item from the query
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name: "polls/results.html"
    

"""
def index(request):
    doesntmatter = Question.objects.all()
    return render(request,"polls/index.html",{"latest_question_list":doesntmatter})


def detail(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question" : question})


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

"""

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError , Choice.DoesNotExist):
        return render(request, "polls/detail.html", { 
            "question": question,
            "error_message": "You didnt pick an option"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))
    