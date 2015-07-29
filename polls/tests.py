import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.



class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_actual_question(self):
        time = timezone.now()
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), True)

    def test_was_published_recently_with_actual_one_day(self):
        time = timezone.now() - datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_actual_one_halfday(self):
        time = timezone.now() - datetime.timedelta(hours=12)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), True)

    def test_was_published_recently_with_actual_two_dayn(self):
        time = timezone.now() - datetime.timedelta(days=2)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
