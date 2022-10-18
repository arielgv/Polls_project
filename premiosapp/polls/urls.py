from django.urls import path

from . import views

app_name = "polls"
#esto evita el hard coding 
urlpatterns = [

    path("", views.IndexView.as_view(template_name="polls/index.html",context_object_name="latest_question_list"), name="index"),
    path("<int:pk>/", views.DetailView.as_view(template_name="polls/detail.html"), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(template_name="polls/results.html"), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]