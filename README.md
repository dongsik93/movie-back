1. 사전준비

```bash
pip install djangorestframework
```

- settings에 rest_framework 를 추가해준다.

```python
INSTALLED_APPS=[
	rest_framework
]
```

-  url에  (api의 버전1)

  path('api/v1/', include('movies.urls'))를 추가해준다.



2. GET /api/v1/genres/

```curl -X GET "http://localhost:8000/api/v1/genres/" -H "accept:application/json"```

- 장르의 목록을 요청 받아서 장르의 id와 name 목록을 json 형태로 뿌려준다.

- urls.py 에 path("genres/", views.genre_list)를 추가 해준다.

- serializers.py 에 from rest_framework import serializers와 모델을 import후에

  MovieSerializers 의 클래스를 생성 해서 쿼리셋을 json데이터로 바꿔줄  Serializers를 만들어 준다.

```python
from django.shortcuts import render, get_object_or_404
from .models import Genre
from .serializers import GenreSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def genre_list(request):
	genres = Genre.objects.all()
	serializer = GenreSerializers(genres, many=True)
	return Response(serializer.data)
```

- GET 방식일때만 api_view화면을 꾸며주는 데코레이터를 붙여준다.

- Genre의 모든 객체들을 가져온다.

- serializer를 통해 QuerySet 을 json데이터로 바꿔준다.

- json데이터를 뿌려준다.



3. GET /api/v1/genres/{genre_pk}/

- 특정 장르의 결과를 응답합니다.

- urls.py에 path("genres/<int:genre_id>/", views.genre_detail)로 url주소를 만들어 준다.

```python
from .models import Genre
from .serializers import GenreDetailSerializers

@api_view(['GET'])
def genre_detail(request, genre_id):
	genre = Genre.objects.get(id=genre_id)
	genre = get_object_or_404(Genre, id=genre_id)
	serializer = GenreDetailSerializers(genre)
	return Response(serializer.data)
```

- 특정 장르의 결과를 json형태로 뿌려주는 함수를 구현한다.



4. GET /api/v1/movies

- 영화 목록을 요청 받아서 다음과 같은 결과를 응답합니다.

- url.py에 path('movies/', views.movie_list) 주소를 만들어준다.

```python
from .models import Movie
from .serializers import MovieSerializers

@api_view(['GET'])
def movie_list(request):
	movies = Movie.objects.all()
	serializer = MovieSerializers(movies, many=True)
	return Response(serializer.data)
```

- 영화 목록을 json데이터로 뿌려주는 함수를 구현한다.



5. GET /api/v1/movies/{movie_pk}

- 특정 영화의 결과를 응답합니다.

- path('movies/<int:movie_id>/', views.movie_detail) 주소를 만들어준다.

```python
@api_view(['GET'])
def movie_detail(request, movie_id):
	movie = get_object_or_404(Movie, id=movie_id)
	serializer = MovieSerializers(movie)
	return Response(serializer.data)
```

- 특정 영화의 json데이터를 뿌려주는 함수를 구현한다.



6. POST /api/v1/movies/{movie_pk}/scores/

- 특정 영화에 평점을 등록합니다. 성공시 아래와 같이 응답합니다.

- 만약, 없는 경로 변수(movie_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.
  필수 필드가 누락된 경우 400 Bad Request 에러를 응답합니다.

- path('movies/<int:movie_id>/scores/', views.score_create) 주소를 만들어준다.

```python
from .models import Score
from .serializers import ScoreSerializers

@api_view(['POST'])
def score_create(request, movie_id):
	movie = get_object_or_404(Movie, id=movie_id)
	serializer = ScoreSerializers(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(movie=movie)
		return Response(serializer.data)
		return Response({'message':'작성되었습니다.'})
```

- 특정 영화에 평점을 등록하는 함수를 구현한다.



7. 평점 디테일,수정,삭제를 구현하는 함수

-  path('scores/<int:score_id>/', views.scores)를 만들어준다.

```python
@api_view(['PUT','DELETE','GET'])        
def scores(request, score_id):
	score = get_object_or_404(Score, id=score_id)
	if request.method == "PUT":
		serializer = ScoreSerializers(data=request.data, instance = score)
		if serializer.is_valid():
			serializer.save()
			return Response({'message':'수정되었습니다.'})
elif request.method =="DELETE":
		score.delete()
		return Response({'message':'삭제되었습니다.'})
	elif request.method =="GET":
		score = get_object_or_404(Score, id=score_id)
		serializer = ScoreSerializers(score)
		return Response(serializer.data)
```

- 특정 평점을 수정합니다. 성공시 아래와 같이 응답합니다.

- 만약, 없는 경로 변수(score_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.
  필수 필드가 누락된 경우 400 Bad Request 에러를 응답합니다.



- 특정 평점을 삭제합니다. 성공시 아래와 같이 응답합니다.

- 만약, 없는 경로 변수(score_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.



- 특정 평점의 상세 페이지의 jsondata 정보를 뿌려주는 것을 만들어준다.