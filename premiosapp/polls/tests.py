
import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question
from polls import views

# Create your tests here.

class QuestionModelTestCase(TestCase):

    def test_recently_published_for_future (self):
        """ this is for future cases of publications .  """
        Fecha = timezone.now() + datetime.timedelta(days=30)
        q = Question(question_text="prueba error", pub_date=Fecha)

        self.assertIs(q.recently_published(), False)
    
    def test_recently_published_for_past (self):
        """ this is for past cases of publications"""
        Fecha = timezone.now() - datetime.timedelta(days=31)
        q = Question(question_text="prueba error", pub_date=Fecha)

        self.assertIs(q.recently_published(), False)
    
    def test_recently_published_present(self):
        """ this test is for present publications and should return True"""
        Fecha= timezone.now() - datetime.timedelta(days=5)
        q = Question(question_text="prueba_error", pub_date=Fecha)

        self.assertIs(q.recently_published(),True)
    
#class IndexViewTestCase(TestCase):

 #   def test_index_view(self):

