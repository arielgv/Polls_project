from django.urls import path
#from .models import Question,Choice
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:question>", views.detail, name="index"),
    path("<int:question>/results/", views.results, name="index"),
    path("<int:question>/vote/", views.vote, name="index")

]