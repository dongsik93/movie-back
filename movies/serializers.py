from rest_framework import serializers
from .models import Genre, Movie, Score

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
