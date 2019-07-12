from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie, Score, MovieCd, MovieDetail, OurMovieCd, OurMovieDetail
from .serializers import GenreSerializers, MovieSerializers, GenreDetailSerializers,ScoreSerializers, MovieCdSerializers, MovieDetailSerializers, OurMovieCdSerializers, OurMovieDetailSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
import requests

import urllib.request as ul
import json
from datetime import date, timedelta, datetime
from django.conf import settings

import urllib.request
from bs4 import BeautifulSoup

# from rest_framework.permissions import IsAuthenticated
# Create your views here.



# @authentication_classes(())
# @permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializers(genres, many = True) # many: 여러개의 자료가 들어있다.
    return Response(serializer.data)

@api_view(['GET'])    
def genre_detail(request,genre_id):
    # genre = Genre.objects.get(id = genre_id)
    genre = get_object_or_404(Genre, id=genre_id)
    serializer = GenreDetailSerializers(genre)
    return Response(serializer.data)
  
@api_view(['GET'])    
def movie_list(request):
    movies = MovieDetail.objects.all()
    serializer = MovieDetailSerializers(movies, many = True)
    return Response(serializer.data) 

@api_view(['GET'])    
def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, id =movie_id)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)

@api_view(['POST'])       
def scores_create(request,movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    serializer = ScoreSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        return Response(serializer.data)
        # return Response({"message":"작성되었습니다."})

@api_view(['PUT','DELETE','GET'])       
def scores(request,score_id):
    score = get_object_or_404(Score, id = score_id)
    if request.method == "PUT" :
        serializer = ScoreSerializers(data=request.data, instance=score)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정되었습니다."})
    elif request.method =="DELETE":
        score.delete()
        return Response({"message":"삭제되었습니다."})
    else :
        serializer = ScoreSerializers(score)
        return Response(serializer.data)

@api_view(['GET'])
def ourmovies_list(request) :
    movies = OurMovieDetail.objects.all()
    serializer = OurMovieDetailSerializers(movies, many = True)
    return Response(serializer.data) 













# 좋아요
# @api_view(['GET'])
# def like(request,id):
#     # 지금 좋아요를 요청하는 유저
#     user = request.user
#     # 좋아요를 누를 영화
#     movie = (모델명).objects.get(id=id)
#     #  사용자가 영화에 좋아요를 눌렀다면
#     if user in movie.(유저와 1:N 걸어준 변수명).all():
#         movie.likes.remove(user)
#     # 사용자가 좋아요를 누르지 않았다면
#     else:
#         movie.likes.add(user)
#     return response('complete')

#     # Movie 와 like 모델 예시
#     class Movie(models.Model):
#         likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie_set", blank=True)
