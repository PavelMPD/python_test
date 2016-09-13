import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now() + datetime.timedelta(days=15)).date())
        self.assertFalse(question.was_published_recently())

    def test_was_published_recently_with_ols_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now() - datetime.timedelta(days=2)).date())
        self.assertFalse(question.was_published_recently())

    def test_was_published_recently_with_recently_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now()).date())
        self.assertTrue(question.was_published_recently())


class QuestionIndexViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_index_view_with_a_past_question(self):
        Question.objects.create(
            question_text="past question", pub_date=(timezone.now() - datetime.timedelta(days=2)).date())
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['questions']), 1)

    def test_index_view_with_a_future_question(self):
        Question.objects.create(
            question_text="future question", pub_date=(timezone.now() + datetime.timedelta(days=1)).date())
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['questions']), 0)


class QuestionDetailViewTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        question = Question.objects.create(
            question_text="future question", pub_date=(timezone.now() + datetime.timedelta(days=5)).date())
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        question = Question.objects.create(
            question_text="past question", pub_date=(timezone.now() - datetime.timedelta(days=5)).date())
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertContains(response, question.question_text)
