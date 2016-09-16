from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.db.models import F
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice
from polls.forms import QuestionCreateForm, QuestionUpdateForm


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions" # question_list by default

    def get_queryset(self):
        questions = Question.objects.filter(pub_date__lte=timezone.now().date()).order_by("-pub_date")[:10]
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

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now().date())

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

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now().date())

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


class QuestionListView(generic.ListView):
    model = Question
    # template_name = "polls/question_list.html"
    context_object_name = "questions"


class QuestionCreateView(generic.CreateView):
    model = Question
    # fields = ["question_text", "pub_date"]  # Specifying both 'fields' and 'form_class' is not permitted.
    template_name = "polls/question_form.html"  # This template name is by default.
    form_class = QuestionCreateForm

    def get_success_url(self):
        return reverse("polls:question_list")

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context["submit_button_name"] = "Create"
        return context

    # def form_invalid(self, form):
    #     response = super(QuestionCreateView, self).form_invalid(form)
    #     return response


class QuestionUpdateView(generic.UpdateView):
    model = Question
    template_name = "polls/question_form.html"
    form_class = QuestionUpdateForm

    def get_success_url(self):
        return reverse("polls:question_list")

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context["submit_button_name"] = "Update"
        return context


class QuestionDeleteView(generic.DeleteView):
    model = Question
    success_url = reverse_lazy("polls:question_list")
    # template_name = "polls/question_confirm_delete.html"
