from rest_framework import serializers
from .models import Genre, Movie, Score, MovieCd, MovieDetail, OurMovieCd, OurMovieDetail

class MovieSerializers(serializers.ModelSerializer):
    # genre = serializers.CharField(source="genre.name")
    class Meta :
        model = Movie
        fields = '__all__'
        
class GenreSerializers(serializers.ModelSerializer): # 장고에 있는 데이터베이스를 제이슨으로 변환
    class Meta :
        model = Genre
        fields = ['id','name']

class GenreDetailSerializers(serializers.ModelSerializer):
    movies = MovieSerializers(source = "movie_set", many=True)
    class Meta :
        model = Genre
        fields = ['id','name','movies']
        
class ScoreSerializers(serializers.ModelSerializer):
    class Meta :
        model = Score
        fields = ['id','content','value']
        
class MovieCdSerializers(serializers.ModelSerializer):
    class Meta :
        model = MovieCd
        fields = ['id','movieCd','rank']
        
class MovieDetailSerializers(serializers.ModelSerializer):
    class Meta :
        model = MovieDetail
        fields = ['id','movieCd','rank','audiAcc','movieNm','showTm','openDt','nationNm','genres','actors','actors_img','actors_role','watchGradeNm','dialog','image_url','large_image','story','rating','Participating','score_reples','score_reple_id','score_reple_like','video']

class OurMovieCdSerializers(serializers.ModelSerializer):
    class Meta :
        model = OurMovieCd
        fields = ['id','movieCd','audiAcc']
        
class OurMovieDetailSerializers(serializers.ModelSerializer):
    class Meta :
        model = OurMovieDetail
        fields = ['id','movieCd','audiAcc','movieNm','showTm','openDt','nationNm','genres','actors','actors_img','actors_role','watchGradeNm','dialog','image_url','large_image','story','rating','Participating','score_reples','average','score_reple_id','score_reple_like']