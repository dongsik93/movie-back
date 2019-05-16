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

from rest_framework.permissions import IsAuthenticated
# Create your views here.

@authentication_classes(())
@permission_classes((IsAuthenticated, ))
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
      
@api_view(['GET'])
def api_request(request):
    global date
    yesterday = date.today() - timedelta(1)

    movieDate = yesterday.strftime('%Y%m%d')
    
    # 일자정보
    int(movieDate)
    
    token = "da527a5a57d79d8c6cfeec3a6521fb67"
    # 영진위 url
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={token}&targetDt={movieDate}"

    request = ul.Request(url)
    
    response = ul.urlopen(request)
    rescode = response.getcode()
    
    if(rescode == 200):
    	responseData = response.read()
    
    result = json.loads(responseData)
    
    MovieCd.objects.all().delete()
    # 리셋
    
    for movie in result.get('boxOfficeResult').get('dailyBoxOfficeList'):
        code = movie.get('movieCd')
        mo = MovieCd.objects.create(
            rank=movie.get('rank'),
            movieCd = movie.get('movieCd'),
            audiAcc = movie.get('audiAcc')
            )
        mo.save()
        
    base_url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd="

    MovieDetail.objects.all().delete()
    # 리셋
    
    
    # themovie api_key
    # api_key = "171fb9b9c08948ca73f8f4dec725dbab"
    
    
    # 네이버 id,secretkey
    client_id = "bzMByT36GfYciVmuwmyy"
    client_secret = "rIt_K8J2V1"
    
    
    
    for movie in MovieCd.objects.all() :
        Cd = movie.movieCd
        url = base_url+Cd
        request = ul.Request(url)
        
        response = ul.urlopen(request)
        rescode = response.getcode()
        
        if(rescode == 200):
        	responseData = response.read()
        
        result = json.loads(responseData)
        
        movieInfo = result.get('movieInfoResult').get('movieInfo')
        
        # 장르리스트
        genres_list = []
        # 장르 for문
        for i in movieInfo.get('genres'):
            genres_list.append(i.get('genreNm'))
    
        # # 감독 한국명
        # directors = (movieInfo.get('directors')[0].get('peopleNm'))
        
        # # 배우리스트
        # actors_list = []
        # # 배우 for문
        # for i in movieInfo.get('actors')[0:3]:
        #     actors_list.append(i.get('peopleNm'))
        # actors_list = " / ".join(actors_list)
    
        # 날짜 datetimefield 형태로 변환
        s = movieInfo.get('openDt')
        date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
        s = date.strftime("%Y-%m-%d")
        
        # 검색단어
        encText = urllib.parse.quote(movieInfo.get('movieNm'))
        
        # themovie url
        # themovie_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=" + encText
        # themovie_request = urllib.request.Request(themovie_url)
        # themovie_response = urllib.request.urlopen(themovie_request)
        # themovie_rescode = themovie_response.getcode()
        # if(themovie_rescode==200):
        #     response_body = themovie_response.read()
        #     themovie_result = json.loads(response_body.decode('utf-8'))
        #     themovie_image = "https://image.tmdb.org/t/p/w500"+themovie_result.get('results')[0].get('poster_path')
        # else:
        #     print("Error Code:" + themovie_rescode)
        
        
        naver_url = f"https://openapi.naver.com/v1/search/movie.json?query=" + encText
        naver_request = urllib.request.Request(naver_url)
        naver_request.add_header("X-Naver-Client-Id",client_id)
        naver_request.add_header("X-Naver-Client-Secret",client_secret)
        
        naver_response = urllib.request.urlopen(naver_request)
        naver_rescode = naver_response.getcode()
        if(naver_rescode==200):
            response_body = naver_response.read()
            naver_result = json.loads(response_body.decode('utf-8'))
            naver_movie_url = naver_result.get('items')[0].get('link')
        else:
            print("Error Code:" + themovie_rescode)
            
        # 줄거리 시작    
        req = requests.get(naver_movie_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        class_p = soup.find('p',{'class':'con_tx'})
        # 줄거리 끝
        
        # 코드 추출 시작
        movie_code = []
        
        for i in range(len(naver_movie_url)-1,-1,-1) :
            if naver_movie_url[i] == "=":
                break
            movie_code.append(naver_movie_url[i])
        
        movie_code.reverse()
        
        movie_code = ''.join(movie_code)
        
        naver_poster_image_url = f"https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+movie_code
        # 코드 추출 끝
        
        # 이미지 링크 시작
        image_req = requests.get(naver_poster_image_url)
        image_soup = BeautifulSoup(image_req.text, 'html.parser')
        
        id_img = image_soup.a.img['src']
        # 이미지 링크 끝
        
        # 배우이름, 사진, 역할 시작
        movie_actors = soup.find('div',{'class':'people'}).ul.find_all('li')
        movie_actors_title = []
        movie_actors_img = []
        movie_actors_role = []
        for movie_actor in movie_actors :
            movie_actors_title.append(movie_actor.a['title'])
            movie_actors_img.append(movie_actor.a.img['src'])
            if movie_actor.dl.dd :
                movie_actors_role.append(movie_actor.dl.dt.text + " / " + movie_actor.dl.dd.text)
            else :
                movie_actors_role.append(movie_actor.dl.dt.text+" / ")
        # 배우이름, 사진, 역할 끝
        
        
        # 평점시작
        id_div = soup.find('div',{'id':'pointNetizenCountBasic'})
        if id_div:
            movie_rating = id_div.text.strip()
        else :
            movie_rating = -1
            
        id_a = soup.find('a',{'id':'pointNetizenPersentBasic'})
        if id_a:
            movie_Participating = id_a.text
        else :
            movie_Participating = -1
        # 평점 끝
        
        # 리뷰 시작
        movie_score_reples = []
        score_reples = soup.find_all('div',{'class':'score_reple'})
        for score_reple in score_reples :
            movie_score_reples.append(score_reple.p.text)
            
        movie_score_reple_ids = []
        for score_reple in score_reples :
            movie_score_reple_ids.append(score_reple.dl.dt.em.a.span.text)
        
        movie_score_reple_likes = []
        reple_likes = soup.find_all('div',{'class':'btn_area'})
        for reple_like in reple_likes :
            movie_score_reple_likes.append(reple_like.strong.span.text)
        
        # 리뷰 끝
        
        # 와이드 이미지 시작
        large_img_url = "https://movie.naver.com/movie/bi/mi/photoView.nhn?code=" + movie_code
        large_image_req = requests.get(large_img_url)
        large_image_soup = BeautifulSoup(large_image_req.text, 'html.parser')
        large_image_find = large_image_soup.find('div',{'class':'rolling_list'})
        large_images =  large_image_find.ul.find_all('li')[:3]
        large_img = []
        for large_image in large_images :
            large_img.append(json.loads(large_image['data-json'])['fullImageUrl886px'])

        # 와이드 이미지 끝

        mo = MovieDetail.objects.create(
                movieNm= movieInfo.get('movieNm'),
                showTm = movieInfo.get('showTm'),
                openDt = s,
                nationNm = movieInfo.get('nations')[0].get('nationNm'),
                genres = genres_list,
                actors = movie_actors_title,
                actors_img = movie_actors_img,
                actors_role = movie_actors_role,
                watchGradeNm = movieInfo.get('audits')[0].get('watchGradeNm'),
                dialog = "false",
                image_url = id_img,
                large_image = large_img,
                story = class_p.text,
                rating = movie_rating,
                Participating = format(float(movie_Participating)/2,".2f"),
                score_reples = movie_score_reples,
                score_reple_id = movie_score_reple_ids,
                score_reple_like = movie_score_reple_likes,
                movieCd = movie.movieCd,
                rank = movie.rank,
                audiAcc = movie.audiAcc, 
                show1 = "false",
                show2 = "false"
            )
        mo.save()
    return Response("??????")


@api_view(['GET'])
def base_api_request(request):
    OurMovieCd.objects.all().delete()
    token = "da527a5a57d79d8c6cfeec3a6521fb67"
    #리셋
    global date
    weekly = date.today()
    for i in range(52):
        weekly -= timedelta(7)
        startday = weekly.strftime('%Y%m%d')
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt=" + str(startday)
        
        request = ul.Request(url)
    
        response = ul.urlopen(request)
        rescode = response.getcode()
        
        if(rescode == 200):
        	responseData = response.read()
        
        result = json.loads(responseData)
        
        # movie = Movie.objects.get_or_create(필드명)
        # 결과값( obeject, True/False) True - Create/ False - Get
        #if movie[1] == True : Create
        #if movie[1] == False : Get
        
        for movie in result.get('boxOfficeResult').get('weeklyBoxOfficeList') :
            code = movie.get('movieCd')
            mo = OurMovieCd.objects.get_or_create(
                movieCd = movie.get('movieCd'),
                )
            if mo[1] :
                mo[0].audiAcc = movie.get('audiAcc')
                mo[0].save()
            print(mo[0])
 
 
 
 
 
    base_url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd="

    OurMovieDetail.objects.all().delete()
    # 리셋
    
    # 네이버 id,secretkey
    client_id = "bzMByT36GfYciVmuwmyy"
    client_secret = "rIt_K8J2V1"
    
    
    
    for movie in OurMovieCd.objects.all() :
        Cd = movie.movieCd
        url = base_url+Cd
        request = ul.Request(url)
        
        response = ul.urlopen(request)
        rescode = response.getcode()
        
        if(rescode == 200):
        	responseData = response.read()
        
        result = json.loads(responseData)
        
        movieInfo = result.get('movieInfoResult').get('movieInfo')
        
        # 장르리스트
        genres_list = []
        # 장르 for문
        for i in movieInfo.get('genres'):
            genres_list.append(i.get('genreNm'))
    

        # 날짜 datetimefield 형태로 변환
        s = movieInfo.get('openDt')
        date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
        s = date.strftime("%Y-%m-%d")
        
        # 검색단어
        encText = urllib.parse.quote(movieInfo.get('movieNm'))
        
        naver_url = f"https://openapi.naver.com/v1/search/movie.json?query=" + encText
        naver_request = urllib.request.Request(naver_url)
        naver_request.add_header("X-Naver-Client-Id",client_id)
        naver_request.add_header("X-Naver-Client-Secret",client_secret)
        
        naver_response = urllib.request.urlopen(naver_request)
        naver_rescode = naver_response.getcode()
        
        if(naver_rescode==200):
            response_body = naver_response.read()
            naver_result = json.loads(response_body.decode('utf-8'))
            naver_movie_url = naver_result.get('items')[0].get('link')
        else:
            print("Error Code:" + themovie_rescode)
            
        # 줄거리 시작    
        req = requests.get(naver_movie_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        class_p = soup.find('p',{'class':'con_tx'})
        # 줄거리 끝
        
        # 코드 추출 시작
        movie_code = []
        
        for i in range(len(naver_movie_url)-1,-1,-1) :
            if naver_movie_url[i] == "=":
                break
            movie_code.append(naver_movie_url[i])
        
        movie_code.reverse()
        
        movie_code = ''.join(movie_code)
        
        naver_poster_image_url = f"https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+movie_code
        # 코드 추출 끝
        
        # 이미지 링크 시작
        image_req = requests.get(naver_poster_image_url)
        image_soup = BeautifulSoup(image_req.text, 'html.parser')
        
        id_img = image_soup.a.img['src']
        # 이미지 링크 끝
        
        # 배우이름, 사진, 역할 시작
        movie_actors = soup.find('div',{'class':'people'}).ul.find_all('li')
        movie_actors_title = []
        movie_actors_img = []
        movie_actors_role = []
        for movie_actor in movie_actors :
            movie_actors_title.append(movie_actor.a['title'])
            movie_actors_img.append(movie_actor.a.img['src'])
            if movie_actor.dl.dd :
                movie_actors_role.append(movie_actor.dl.dt.text + " / " + movie_actor.dl.dd.text)
            else :
                movie_actors_role.append(movie_actor.dl.dt.text+" / ")
        # 배우이름, 사진, 역할 끝
        
        
        # 평점시작
        id_div = soup.find('div',{'id':'pointNetizenCountBasic'})
        if id_div:
            movie_rating = id_div.text.strip()
        else :
            movie_rating = -1
            
        id_a = soup.find('a',{'id':'pointNetizenPersentBasic'})
        if id_a:
            movie_Participating = id_a.text
        else :
            movie_Participating = -1
        # 평점 끝
        
        # 리뷰 시작
        movie_score_reples = []
        score_reples = soup.find_all('div',{'class':'score_reple'})
        for score_reple in score_reples :
            movie_score_reples.append(score_reple.p.text)
            
        movie_score_reple_ids = []
        for score_reple in score_reples :
            movie_score_reple_ids.append(score_reple.dl.dt.em.a.span.text)
        
        movie_score_reple_likes = []
        reple_likes = soup.find_all('div',{'class':'btn_area'})
        for reple_like in reple_likes :
            movie_score_reple_likes.append(reple_like.strong.span.text)
        # 리뷰 끝

        # 와이드 이미지 시작
        large_img_url = "https://movie.naver.com/movie/bi/mi/photoView.nhn?code=" + movie_code
        large_image_req = requests.get(large_img_url)
        large_image_soup = BeautifulSoup(large_image_req.text, 'html.parser')
        large_image_find = large_image_soup.find('div',{'class':'rolling_list'})
        large_images =  large_image_find.ul.find_all('li')[:3]
        large_img = []
        for large_image in large_images :
            large_img.append(json.loads(large_image['data-json'])['fullImageUrl886px'])

        # 와이드 이미지 끝


        mo = OurMovieDetail.objects.create(
                movieNm= movieInfo.get('movieNm'),
                showTm = movieInfo.get('showTm'),
                openDt = s,
                nationNm = movieInfo.get('nations')[0].get('nationNm'),
                genres = genres_list,
                actors = movie_actors_title,
                actors_img = movie_actors_img,
                actors_role = movie_actors_role,
                watchGradeNm = movieInfo.get('audits')[0].get('watchGradeNm'),
                dialog = "false",
                image_url = id_img,
                large_image = large_img,
                story = class_p.text,
                rating = movie_rating,
                Participating = format(float(movie_Participating)/2,".2f"),
                score_reples = movie_score_reples,
                score_reple_id = movie_score_reple_ids,
                score_reple_like = movie_score_reple_likes,
                movieCd = movie.movieCd,
                audiAcc = movie.audiAcc, 
                show1 = "false",
                show2 = "false"
            )
        mo.save()            
        
        
        
    return Response("??")













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
