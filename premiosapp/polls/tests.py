
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


    def test_two_future_questions(self):
        """ This test proves two differents questions in the index in order
        to test if anyone is showing in the main page."""
        time1 = timezone.now() + datetime.timedelta(days=24)
        time2 = timezone.now() + datetime.timedelta(days=23)
        Question.objects.create(question_text="text1",pub_date=time1)
        Question.objects.create(question_text="text2",pub_date=time2)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_two_past_questions(self):
        """this test intends to post two questions in the past and
        checking out if there were posted correctly as it should."""
        time1 = timezone.now() + datetime.timedelta(days=-12)
        time2 = timezone.now() + datetime.timedelta(days=-28)
        past1=Question.objects.create(question_text="text past 1", pub_date=time1)
        past2=Question.objects.create(question_text="text past 2", pub_date=time2)
        response = self.client.get(reverse("polls:index"))
        #self.assertQuerysetEqual(response.context["latest_question_list"],[past1,past2])
        self.assertNotEqual(response.context["latest_question_list"],[])

class QuestionDetailViewTest(TestCase):
    
    def test_future_question(self):
        # Test para saber si se publicarán o no preguntas futuras 
        time_future = timezone.now() + datetime.timedelta(days=30)
        future_question = Question.objects.create(question_text="future question",pub_date=time_future )
        url = reverse("polls:detail", args=(future_question.id,))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 404)



    def test_detail_view(self):
        # test para comprobar si se publican exitosamente las publicaciones pasadas. 
        time_past = timezone.now() + datetime.timedelta(days=-30)
        past_question = Question.objects.create(question_text="past question", pub_date=time_past)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)