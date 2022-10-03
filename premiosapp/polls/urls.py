from django.urls import path
#from .models import Question,Choice
from . import views

app_name = "polls"
#esto evita el hard coding 

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")

]