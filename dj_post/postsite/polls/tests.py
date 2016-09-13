import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now() + datetime.timedelta(days=15)).date())
        self.assertFalse(question.was_published_recently())

    def test_was_published_recently_with_ols_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now() - datetime.timedelta(days=2)).date())
        self.assertFalse(question.was_published_recently())

    def test_was_published_recently_with_recently_question(self):
        question = Question(question_text="some text", pub_date=(timezone.now()).date())
        self.assertTrue(question.was_published_recently())
