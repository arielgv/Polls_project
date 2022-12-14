from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date= models.DateTimeField("publication date")

    def __str__(self):
        return self.question_text
    
    def recently_published(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=30)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text