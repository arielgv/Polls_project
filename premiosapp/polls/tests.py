
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
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

def create_question(the_question,the_date):
    """Its for create fastly a question, variable the_question is for the text question, 
    and the date its number of days offset, negative for days in past
    positive for days in future"""
    t = Question.objects.create(question_text=str(the_question), pub_date=timezone.now()+datetime.timedelta(days=the_date))
    return t 

class QuestionIndexViewTestCase(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
    




    def test_not_publish_future_posts(self):
        """ This test intends to publish a post submited in the future"""
        fecha = timezone.now() + datetime.timedelta(days=-10)
        q = Question.objects.create(question_text="no importa", pub_date = fecha )
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(response.context["latest_question_list"],[q])

    def test_past_questions(self):
        """ This test checks if the past questions are displayed correctly"""
        fecha = timezone.now() - datetime.timedelta(days=10)
        w=Question.objects.create(question_text="Past question",pub_date=fecha)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_question_list'],[w])


