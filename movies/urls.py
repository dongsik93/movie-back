from django.urls import path
from . import views

urlpatterns = [
    path('genres/',views.genre_list),
    path('genres/<int:genre_id>/',views.genre_detail),
    path('movies/',views.movie_list),
    path('movies/<int:movie_id>/',views.movie_detail),
    path('movies/<int:movie_id>/scores/',views.scores_create),
    path('scores/<int:score_id>/',views.scores),
    # path('rest-auth/registration/', views.registration),
    path('api_request/',views.api_request),
    path('base_api_request/',views.base_api_request),
    path('ourmovies/',views.ourmovies_list),
]
