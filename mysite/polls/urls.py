from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # EX: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # EX: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # EX /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # EX: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]