from django.urls import path
from . import views

urlpatterns = [
    path('genres/',views.genre_list),
    path('genres/<int:genre_id>/',views.genre_detail),
    path('movies/',views.movie_list),
    path('movies/<int:movie_id>/',views.movie_detail),
    path('movies/<int:movie_id>/scores/',views.scores_create),
    path('scores/<int:score_id>/',views.scores),
]
