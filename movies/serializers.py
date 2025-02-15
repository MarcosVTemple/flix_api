from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
from actors.models import Actor
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser inferior a 1900!"
            )
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
    
class MovieListDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
        
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return rate
        return None
