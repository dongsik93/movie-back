from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    
class Score(models.Model):
    content = models.CharField(max_length=50)
    value = models.IntegerField()
    movie =  models.ForeignKey(Movie, on_delete = models.CASCADE)
    
    
class MovieCd(models.Model):
    # 영화코드
    movieCd = models.TextField()
    # 순위
    rank = models.TextField()
    # 누적관객수
    audiAcc = models.TextField()
    
class MovieDetail(models.Model):
    # 영화이름
    movieNm = models.CharField(max_length=100)
    # 상영시간
    showTm = models.IntegerField()
    # 개봉일자
    openDt = models.DateField()
    # 국가명
    nationNm = models.CharField(max_length=100)
    # 장르
    genres = models.CharField(max_length=100)
    # 영화배우들
    actors = models.CharField(max_length=100)
    # 영화배우 사진
    actors_img = models.CharField(max_length=100)
    # 영화 배우 역할
    actors_role = models.CharField(max_length=100)
    # 관람등급
    watchGradeNm = models.CharField(max_length=100)
    # image_url
    image_url = models.CharField(max_length=100)
    # large_image
    large_image = models.CharField(max_length=200)
    # 줄거리
    story = models.TextField()
    # 평점
    rating = models.CharField(max_length=100)
    # 평점 참여 
    Participating = models.CharField(max_length=100)
    # 리뷰
    score_reples = models.TextField()
    # 리뷰 아이디
    score_reple_id = models.TextField()
    # 리뷰 공감
    score_reple_like = models.TextField()
    
    dialog = models.CharField(max_length=100)
    
    # for문을 이용해서 MovieCd의 정보를 가져와서 저장할 스키마
    # 영화코드
    movieCd = models.TextField()
    # 순위
    rank = models.TextField()
    # 누적관객수
    audiAcc = models.TextField()
    
    show1=models.CharField(max_length=100)
    
    show2=models.CharField(max_length=100)

    video=models.CharField(max_length=100)
    
    
class OurMovieCd(models.Model):
    # 영화코드
    movieCd = models.TextField()
    # 누적관객수
    audiAcc = models.TextField(null=True)

class OurMovieDetail(models.Model):
    # 영화이름
    movieNm = models.CharField(max_length=100)
    # 상영시간
    showTm = models.IntegerField(null=True)
    # 개봉일자
    openDt = models.DateField(null=True)
    # 국가명
    nationNm = models.CharField(null=True,max_length=100)
    # 장르
    genres = models.CharField(null=True,max_length=100)
    # 영화배우들
    actors = models.CharField(null=True,max_length=100)
    # 영화배우 사진
    actors_img = models.CharField(null=True,max_length=100)
    # 영화 배우 역할
    actors_role = models.CharField(null=True,max_length=100)
    # 관람등급
    watchGradeNm = models.CharField(null=True,max_length=100)
    # image_url
    image_url = models.CharField(null=True,max_length=100)
    # large_image
    large_image = models.CharField(null=True,max_length=200)
    # 줄거리
    story = models.TextField(null=True)
    # 평점
    rating = models.CharField(null=True,max_length=100)
    # 평점 참여 
    Participating = models.CharField(null=True,max_length=100)
    # 리뷰
    score_reples = models.TextField(null=True)
    # 리뷰 아이디
    score_reple_id = models.TextField(null=True)
    # 리뷰 공감
    score_reple_like = models.TextField(null=True)
    
    dialog = models.CharField(null=True,max_length=100)
    
    # for문을 이용해서 MovieCd의 정보를 가져와서 저장할 스키마
    # 영화코드
    movieCd = models.TextField()
    # 누적관객수
    audiAcc = models.TextField()
    
    show1=models.CharField(max_length=100)
    
    show2=models.CharField(max_length=100)

    # 평균평점
    average = models.FloatField(null=True)
    
    # 좋아요
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "like_post_set", blank=True)
    
    video=models.CharField(max_length=100)

    
    
# # 우리 사이트에서 직접 매기는 평점 모델
# class Score(models.Model):
#     # 평점 코멘트
#     content = models.CharField(max_length=100)
#     # 평점
#     value = models.IntegerField()
#     # 영화 와 1:N 관계
#     movie = models.ForeignKey(MovieDetail, on_delete=models.CASCADE)
#     # 유저 와 1:N 관계
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # 코멘트 단 시간
#     created_at = models.DateTimeField(auto_now_add=True)