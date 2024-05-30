from . import views
from django.urls import include, path

# In our poll application, we have the following four views:

# Question “index” page – displays the latest few questions.
# Question “detail” page – displays a question text, with no results but with a form to vote.
# Question “results” page – displays results for a particular question.
# Vote action – handles voting for a particular choice in a particular question.


app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


