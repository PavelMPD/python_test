from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions" # question_list by default

    def get_queryset(self):
        questions = Question.objects.order_by("-pub_date")[:5]
        return questions

# def index(request):
#     questions = Question.objects.order_by("-pub_date")[:5]
#     template_name = "polls/index.html"
#     context = {
#         "questions": questions,
#     }
#     return render(request, template_name, context)


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     template_name = "polls/detail.html"
#     context = {
#         "question": question,
#     }
#     return render(request, template_name, context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {question: question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST["choice"]
    except KeyError:
        context = {
            "question": question,
            "error_message": "You didn't select a choice."
        }
        return render(request, "polls/detail.html", context)
    else:
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes = F("votes") + 1
        choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
