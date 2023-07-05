from django.urls import path

from . import views

app_name = "polls2"

urlpatterns = [
    # ex: /polls2/
    path("", views.index, name="index"),
    # ex: /polls2/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls2/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls2/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /polls2/givno/
    path("givno", views.givno, name="my_givno"),
]
